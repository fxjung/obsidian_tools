import logging
import asyncio
import functools as ft
import re
import googleapiclient.discovery

from pathlib import Path
from urllib import parse as urlparse
from minotaur import Inotify, Mask

from obsidian_tools.config import api_key

log = logging.getLogger(__name__)

api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=api_key
)


def handle_match(match, short=False):
    try:
        url = match[0]

        if short:
            vid = (
                urlparse.urlparse(urlparse.urlparse(url).query).path.lstrip("/").strip()
            )
        else:
            vid = urlparse.parse_qs(urlparse.urlparse(url).query)["v"][0].strip()
        request = youtube.videos().list(part="snippet", id=vid)
        response = request.execute()

        assert len(response["items"]) == 1
        video_title = response["items"][0]["snippet"]["title"]
        channel_title = response["items"][0]["snippet"]["channelTitle"]
        new_text = f"[{video_title} ({channel_title})]({url})"
        return new_text
    except:
        print(f"Unable to enhance link {url} with {vid}")
        return match[0]


def replace_youtube_links(text):
    text = re.sub(
        r"(?![^(]*\))(((https|http)://)?(www\.)?youtube\.[a-z]+/[^ \n]+)",
        handle_match,
        text,
    )

    text = re.sub(
        r"(?![^(]*\))(((https|http)://)?(www\.)?youtu.be/[^ \n]+)",
        ft.partial(handle_match, short=True),
        text,
    )
    return text


async def main(target: Path):
    with Inotify(blocking=False) as n:
        n.add_watch(target, Mask.MODIFY)
        async for evt in n:
            await asyncio.sleep(3)

            old_text = target.read_text()
            new_text = replace_youtube_links(old_text)
            if new_text != old_text:
                target.write_text(new_text)
            log.debug(evt)
