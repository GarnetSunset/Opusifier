# Opusifier
A program that uses ffmpeg to convert music files to opus at equivalent bitrates.

[![forthebadge](http://forthebadge.com/images/badges/made-with-crayons.svg)](http://forthebadge.com)

## What's the point?
Opus can deliver MP3 quality at a tenth of the size. You save a ton of space in the long run.

## Options!

By appending r to the end of "opusiFier.py", the original files will be removed after conversion, only if they succeed.
"opusiFier.py r"

By appending p to the end of "opusiFier.py", the folder where the previous music was stored will be PURGED.
"opusiFier.py p"

### Directory Selection
Either put music in the "music" folder in script root, or create a file called "directory.ini" containing the directory.

## Requirements Install

Python Requirements can be grabbed by either running the requirements file for your platform, or, typing

pip install -r Requirements.txt

#### Download FFMPEG Manually
https://ffmpeg.zeranoe.com/builds/

Extract to the directory of the script.

#### Bugs

Japanese Filenames Don't Work... Yet.
