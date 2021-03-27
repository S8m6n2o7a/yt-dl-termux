#!/bin/bash



cd $HOME
cd Downloads
echo "Welcome to youtube mp3 downloader"
echo -e "enter youtube \e[0;31mlink\e[0m 👇"
read link
youtube-dl --extract-audio --audio-format mp3 $link
echo -e "Your song in \e[0;35m downloader\e[0m folder"
echo -e "\e[0;31mThank\e[0m\e[1;33m you\e[0m \e[0;32mfor\e[0m \e[0;31musing\e[0m \e[0;34myt\e[0m \e[0;35mdownloader\e[0m"
