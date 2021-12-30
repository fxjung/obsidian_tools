from pathlib import Path

from obsidian_tools.watch import handle_match, replace_youtube_links, main


def test_replace_youtube_links():
    text_pre = (Path(__file__).parent / "test_data" / "watch_test_pre.md").read_text()
    text_post = (Path(__file__).parent / "test_data" / "watch_test_post.md").read_text()
    new_text = replace_youtube_links(text_pre)
    assert new_text == text_post
    print(new_text)
