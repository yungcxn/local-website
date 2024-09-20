#!/bin/bash

cd ~/local-website

# Check if $2 (start time) is set, and use -copyts to preserve timestamps when using -ss
if [ -n "$2" ]; then
    ffmpeg -re -ss "$2" -copyts -i ./video/$1 -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://can.fritz.box/live
else
    ffmpeg -re -i ./video/$1 -c:v libx264 -preset veryfast -maxrate 6000k -bufsize 12000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://can.fritz.box/live
fi
