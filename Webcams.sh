#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -d /dev/video0 -r 480x360 --no-banner --set brightness=20% -S 20 /home/pi/MVP/pictures/cam1Left/$DATE.jpg

fswebcam -d /dev/video1 -r 480x360 --no-banner --set brightness=20% -S 20 /home/pi/MVP/pictures/cam2Right/$DATE.jpg