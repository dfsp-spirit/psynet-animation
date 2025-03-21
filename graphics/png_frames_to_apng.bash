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

# read the frame rate from the command line
if [ -n "$1" ]; then
    # if $1 is "-h" or "--help", print help message
    if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then

        echo "Convert a sequence of PNG frames to an animated PNG (APNG) file."
        echo "----------------------------------------------------------------"
        echo "Usage: $0 [[frame_rate] output_file]"
        echo "This script requires ffmpeg to be installed and available on the system path."
        echo "* frame_rate: The number of frames per second in the output animation. Positive integer, defaults to 2."
        echo "* output_file: The name of the output APNG file. Defaults to 'animated.png'."
        exit
    fi

    # check if the input is a positive integer
    if ! [[ "$1" =~ ^[0-9]+$ ]]; then
        echo "Error: The frame rate must be a positive integer."
        exit
    fi
    if [ -n "$2" ]; then
        output_file="$2"
    fi

    fps_anim="$1"
else
    fps_anim=2  # default frame rate
fi


echo "Converting frames to output file '${output_file}' with framerate ${fps_anim}..."
ffmpeg -y -framerate $fps_anim -i "frame_%3d.png" -plays 0 -vf "fps=${fps_anim}" -f apng "${output_file}"
echo "Conversion complete. Check output file, e.g. run: 'firefox ${output_file}'"