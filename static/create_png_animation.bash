#!/bin/sh

for color in {"gray","red","green","blue","yellow","purple","cyan","orange","brown","pink"}; do
    echo "Converting ${color} bird frames to to bird${color}_animated.png"
    ffmpeg -framerate 2 -i bird${color}_frame%d.png -plays 0 bird${color}_animated.png
done
