<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

# Obsidian Tools
Collection of helpers for [Obsidian](https://obsidian.md/).

## Current features
- Watch a single markdown file and replace YouTube URLs with proper Markdown links using 
  "Video title (Channel name)" as link text. File watch is done using inotify, Video info is 
  retrieved through the YouTube Data API, requiring a Google API Key.

## Prerequisites
- Linux (due to inotify)
- Python 3.10
- `pip`

## Installation
```bash
git clone git@github.com:fxjung/obsidian_tools.git
cd obsidian_tools
pip install -e .
pytest
```

## Usage
- Watch a file containing YouTube URLs and replace with proper links on change and logging detailed info to the console:
  ```bash
  obsidian-tools --debug watch ~/obsidian/vault/YouTube.md
  ```