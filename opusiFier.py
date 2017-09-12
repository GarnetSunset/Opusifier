from shutil import copyfile
import os
import re
import sys

def osVersion(owd):
    if os.name == 'nt':
        ffBin = owd+"/ffmpeg/ffmpeg-latest-win64-static/bin/ffmpeg.exe"
    else:
        try:
            os.system('ffmpeg')
        except:
            breaker = True
        else:
            ffBin = "ffmpeg"

def options(option):
    if(option == "-p"):
        purge = True
    if(option == "-r"):
        rmFile = True

owd = os.getcwd()

if os.path.isfile("directory.ini"):
    musicDir = open('directory.ini').read()
else:
    musicDir = owd + "/music"
    if not os.path.exists("music"):
        os.makedirs("music")

osVersion(owd)

if not os.path.exists("ffmpeg") and os.name == 'nt':
    print("Go get ffmpeg please. Or use the batch.")
    break()

dragNDrop = ''.join(sys.argv[1:2])
dragNDrop2 = ''.join(sys.argv[2:3])

if dragNDrop == '-h':
    print("Welcome to the Help Menu\n-h: Help\n-p: Purge Old Files\n-r: Remove Original Files After Use")

if dragNDrop != '':
    options(dragNDrop)

if dragNDrop2 != '':
    options(dragNDrop2)
