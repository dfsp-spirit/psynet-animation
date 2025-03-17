#!/bin/bash
#
# Generate the animated APNG files from the individual frames.
#
# This script should be run from the 'source_images' directory.
# It requires ffmpeg to be installed. Use the following command to install it:
#
#  sudo apt-get install ffmpeg
#
#

output_dir="../static"

echo "Generating animated PNG files from individual frames."
echo "Will save output to directory: ${output_dir}"

if [ ! -d "$output_dir" ]; then
    echo "Please run this script from the 'source_images' directory and make sure the output directory exists."
    exit 1
fi

for color in "gray" "green" "orange" "purple" "yellow"; do
    echo "Converting ${color} bird frames to to bird${color}_animated.png"
    ffmpeg -y -framerate 2 -i bird${color}_frame%d.png -plays 0 -vf "fps=2" -f apng "${output_dir}/bird${color}_animated.png"
done

echo "Script done. Check output above for any errors."

