#!/usr/bin/env python3

import subprocess

print('''	 +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+
   		 |Y|t|D|o|w|n|l|o|d|e|r| |F|o|r |L|i|n|u|x|
   		 +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+
           		 +-+-+ +-+-+-+-+-+-+-+-+-+
          	         |b|y| |S|8|m|6|n|2|o|7|a|
           		 +-+-+ +-+-+-+-+-+-+-+-+-+
''')

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

