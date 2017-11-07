import itertools
import os
import shutil
import sys
import threading
import time

def loading():
    for s in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + s)
        sys.stdout.flush()
        time.sleep(0.1)

def options(option):
    global purge
    global rmFile
    if(option == "p"):
        purge = True
    if(option == "r"):
        rmFile = True

def osVersion(owd):
    global ffBin
    if os.name == 'nt':
        try:
            os.system('ffmpeg')
            os.system('cls')
        except:
            ffBin = owd+"/ffmpeg/ffmpeg-latest-win64-static/bin/ffmpeg.exe"
        else:
            ffBin = "ffmpeg"
    else:
        try:
            os.system('ffmpeg')
            os.system('clear')
        except:
            breaker = True
        else:
            ffBin = "ffmpeg"

def purger():
    youSure = raw_input("Are you sure?\nType \"Yes\" if you're sure.> ")
    if(youSure == "Yes"):
        shutil.rmtree(musicDir)
        os.makedirs(musicDir)
        sys.exit()
    else:
        print("Continuing without Deletion")
        sys.exit()

afterSize = 0
beforeSize = 0
done = False
ext = [".mp3", ".ogg", ".m4a", ".flac"]
noRepeat = 0
owd = os.getcwd()
purge = False
rmFile = False

if os.path.isfile("directory.ini"):
    musicDir = open('directory.ini').read()

else:
    musicDir = owd + "/music"
    if not os.path.exists("music"):
        os.makedirs("music")

osVersion(owd)

if not os.path.exists("ffmpeg") and os.name == 'nt' and ffBin != "ffmpeg":
    print("Go get ffmpeg please. Or use the batch.")
    sys.exit()

dragNDrop = ''.join(sys.argv[1:2])
dragNDrop2 = ''.join(sys.argv[2:3])

if dragNDrop == 'h':
    print("Welcome to the Help Menu\nh: Help\np: Purge Old Files\nr: Remove Original Files After Use")
    raw_input("\nPress Enter to quit...")
    sys.exit()

if dragNDrop != '':
    options(dragNDrop)

if dragNDrop2 != '':
    options(dragNDrop2)

if dragNDrop != '':
    if(purge == True):
        purger()

g = threading.Thread(target=loading)
g.start()

for dname, dirs, files in os.walk(musicDir):
    for fname in files:
        fpath = os.path.join(dname, fname)
        if fname.endswith(tuple(ext)):
            stopPoint = fpath.rfind('.')
            songName = fpath[:stopPoint]
            os.system(ffBin + " -loglevel panic -y -i \"" + fpath + "\" -acodec libopus -vbr on \"" + songName +".opus\"")
            try:
                beforeSize += os.path.getsize(fpath)
                afterSize += os.path.getsize(songName + ".opus")
            except:
                if(noRepeat == 0):
                    noRepeat = 1
            if dragNDrop != '':
                if(rmFile == True):
                    try:
                        os.remove(fpath)
                    except:
                        if(noRepeat == 0):
                            print("Probably a Japanese file, it won't go through conversion.")

afterSize = afterSize/1000000
beforeSize = beforeSize/1000000
done = True

print("\nAll done! Your music library went from being " + str(beforeSize) + "MBs, to being " + str(afterSize) + "MBs, congrats!")
raw_input("\nPress Enter to continue...")
