#!/bin/bash


echo "Downloading requirments"

termux-setup-storage
sleep 2
apt-get -y update
apt-get -y upgrade
pip install --upgrade pip
apt autoremove
apt-get -y install python
pip install youtube-dl
echo "Completed"
chmod 777 yt-meadia.py
./yt-meadia.py
