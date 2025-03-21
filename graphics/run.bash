#!/bin/bash
#
# Wrapper script to run both `node anim_svg_to_png_frames.js` and `png_frames_to_apng.bash` to convert an animated SVG to an animated PNG.
#
# Currently does not support all the command line options of the individual scripts.

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found, please install it."
    exit
fi

input_file="$1"
if [ ! -f "$input_file" ]; then
    echo "Error: File '$input_file' not found."
    exit
fi

# construct output file name by replacing file extension '.svg' with '.png'
output_file="${input_file/.svg/.png}"

# delete frames in the temporary directory if they exist. Do not delete the directory itself.
# This is needed in case old frames are present from a previous run.
rm -f ./frames_tmp/frame_*.png


# Convert the animated SVG to a sequence of PNG frames
node anim_svg_to_png_frames.js --svgFile "$input_file" --outDir "./frames_tmp"
./png_frames_to_apng.bash 2 "${output_file}" "./frames_tmp"



