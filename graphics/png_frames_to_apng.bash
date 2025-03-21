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

# Default values if no command line args given
output_file="animated.png"
input_dir="."
fps_anim=2  # default frame rate

# read the frame rate from the command line
if [ -n "$1" ]; then
    # if $1 is "-h" or "--help", print help message
    if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then

        echo "Convert a sequence of PNG frames to an animated PNG (APNG) file."
        echo "----------------------------------------------------------------"
        echo "Usage: $0 [frame_rate [output_file [input_dir]]]"
        echo "This script requires ffmpeg to be installed and available on the system path."
        echo "* frame_rate: The number of frames per second in the output animation. Positive integer, defaults to 2."
        echo "* output_file: The name of the output APNG file. Defaults to 'animated.png'."
        echo "* input_dir: The directory containing the input PNG frames. Defaults to the current directory. Frames must be named 'frame_001.png', 'frame_002.png', etc. (You can start with index 000 or 001.)"
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
    if [ -n "$3" ]; then
        input_dir="$3"
    else
        input_dir="."
    fi

    fps_anim="$1"
fi


echo "Converting frames in directory '${input_dir}' to output file '${output_file}' with framerate ${fps_anim}..."
ffmpeg -y -framerate $fps_anim -i "${input_dir}/frame_%3d.png" -plays 0 -vf "fps=${fps_anim}" -f apng "${output_file}"
echo "Conversion complete. Check output file, e.g. run: 'firefox ${output_file}'"