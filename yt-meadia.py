#!/usr/bin/env python3

import subprocess

subprocess.run('figlet -f slant "Yt Video/Music Downloder For Linux by S8m6n2o7a"', shell=True)

choice = input("what you want to download video or music v/m:   ")
lchoice = str.lower(choice)

if lchoice == "v" :
	subprocess.run('chmod 777 video.sh', shell=True)
	subprocess.run('./video.sh', shell=True)
elif lchoice == "m" :
	subprocess.run('chmod 777 music.sh', shell=True )
	subprocess.run('./music.sh', shell=True)
else :
	print("Worng input")

