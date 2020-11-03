#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo "Aborting Image Capture, missing dice kind argument"
    echo "Usage: ${0} <dice-kind> <dice-face>"
    exit 0
fi

DICE_KIND=$1
DICE_FACE=$2

DATE=$(date | sed 's/ //g')
echo $DATE

filename=images/${DICE_KIND}/${DATE}_${DICE_KIND}_${DICE_FACE}.jpg
echo $filename

fswebcam -r 640x480 -S 3 -D 1 --set sharpness=6 --set Focus --no-banner ${filename}
