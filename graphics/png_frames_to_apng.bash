#!/bin/bash
#
# Use ffmpeg to convert a sequence of PNG frames to an animated PNG (APNG) file.
#

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found, please install it."
    exit
fi

output_file="animated.png"
fps_anim=2
echo "Converting frames to ${output_file} with framerate ${fps_anim}..."
ffmpeg -y -framerate $fps_anim -i "frame_%3d.png" -plays 0 -vf "fps=${fps_anim}" -f apng "${output_file}"