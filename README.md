# Danbooru Image Grabber

This is an updated Python 3 fork of the [original repo made by uncountablecat](https://github.com/uncountablecat/danbooru-grabber). It downloads media (images *and* videos) from [Danbooru](https://danbooru.donmai.us/).

*WARNING: You may end up downloading pictures that are NSFW depending on the tags you use. So use it wisely.*

## Usage

On your terminal, simply go to the directory where you have installed this script. Then, run `python3 grabber.py`. The program will then prompt you to:
1. provide the tags corresponding to the media you want to download (up to two[^1]), and
2. provide the number of pages of media you want to download.
The program will then mass-download pictures up to the page nunmber you specify. If you wish to terminate the program early, run `Ctrl-C` on Windows and `Command-.` on Mac.
[^1]: you need premium for more tags, and I'm poor

By default, the program will create a new folder at this directory, called `images`, if it has not already been created. You may customize this within `grabber.py`; the corresponding variable to change is `image_folder`. After that, the program will create another folder, within `images`, that is named after the tags you provide.

## Prerequisites
- You need to [have Python 3 installed](https://www.python.org/downloads/).
- You will also need a Python module called [requests](http://docs.python-requests.org/en/latest/). If you have already installed PIP, simply run `pip install requests`.
