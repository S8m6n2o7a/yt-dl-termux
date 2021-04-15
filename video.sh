#!/bin/bash


cd $HOME
cd storage/downloads
figlet -f slant "Welcome to youtube video downloader"
toilet -f term -F border --gay "Enter youtube link 👇"
read link
youtube-dl -f mp4 $link
toilet -f term -F border --gay "Your video in downloader folder"
toilet -f term -F border --gay "Thankyou for using yt downloader"
