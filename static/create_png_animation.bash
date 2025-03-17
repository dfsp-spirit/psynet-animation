#!/bin/sh

#for color in "gray" "green" "orange" "purple" "yellow"; do
for color in "yellow"; do
    echo "Converting ${color} bird frames to to bird${color}_animated.png"
    ffmpeg -framerate 2 -i bird${color}_frame%d.png -plays 0 -vf "fps=2" -f apng "bird${color}_animated.png"
    #ffmpeg -framerate 2 -i "bird${color}_frame%03d.png" -vf "fps=2" -plays 0 "bird${color}_animated.png"
done
