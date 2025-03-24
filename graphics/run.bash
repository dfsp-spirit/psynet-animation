#!/bin/bash
#
# Wrapper script to run both `node anim_svg_to_png_frames.js` and `png_frames_to_apng.bash` to convert an animated SVG to an animated PNG.
#
# Currently does not support all the command line options of the individual scripts.
# It uses fixed temporary dictionary `./frames_tmp` to store the PNG frames.

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found, please install it."
    exit
fi

# Check if node is installed
if ! command -v node &> /dev/null
then
    echo "node could not be found, please install it."
    exit
fi

# Function to display help message
show_help() {
    echo "Convert an animated SVG to an animated PNG (APNG) file."
    echo "-------------------------------------------------------"
    echo "Usage: $0 [--numframes <numframes>] [--delay <delay>] [--outputfile <output_file>] [--framerate <frame_rate>] [--help] <inputfile.svg>"
    echo "This script requires ffmpeg and node to be installed and available on the system path."
    echo "* --numframes: The number of frames to capture from the input SVG animation. Positive integer, defaults to 10."
    echo "* --delay: The delay between frames when capturing screenshots from the input SVG animation. Positive integer (in ms), defaults to 100."
    echo "* --outputfile: The name of the output APNG file. Defaults to the name of the input file with the file extension '.svg replaced by '.png'."
    echo "* --framerate: The number of frames per second in the output animation. Positive integer, defaults to 2."
    echo "* --help: Show this help message and exit."
    echo "* inputfile.svg: The input animated SVG file to be converted to an animated PNG. Required. Must have file extension '.svg' unless --outputfile is specified."
    echo "Example: $0 --framerate 10 --outputfile animation_out.png input.svg"
    exit
}

delay=100   # delay in milliseconds between frames, passed to JS script
numframes=10  # number of frames, passed to JS script
framerate=2 # default frame rate for output APNG, passed to bash script/ffmpeg
input_file=""
output_file=""

# Parse named arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --numframes)
            if [[ "$2" =~ ^[0-9]+$ ]]; then
                numframes="$2"
                shift
            else
                echo "Error: The number of animation frames to capture from the input SVG animation given with '--numframes' must be a positive integer."
                exit 1
            fi
            ;;
        --delay)
            if [[ "$2" =~ ^[0-9]+$ ]]; then
                delay="$2"
                shift
            else
                echo "Error: The delay between frames when capturing screenshots from the input SVG animation given with '--delay' must be a positive integer (in ms)."
                exit 1
            fi
            ;;
        --framerate)
            if [[ "$2" =~ ^[0-9]+$ ]]; then
                framerate="$2"
                shift
            else
                echo "Error: The output APNG framerate given with '--framerate' must be a positive integer."
                exit 1
            fi
            ;;
        --outputfile)
            output_file="$2"
            shift
            ;;
        --help)
            show_help
            ;;
        *)
            input_file="$1"
            ;;
    esac
    shift
done

if [ ! -n "$input_file" ]; then
    show_help
fi


if [ ! -f "$input_file" ]; then
    echo "Error: Input SVG file '$input_file' not found."
    exit
fi

# Construct output file name by replacing file extension '.svg' with '.png'
if [ -z "$output_file" ]; then
    output_file="${input_file/.svg/.png}"
fi

# Double check that output file name is not identical to input file name
if [ "$input_file" == "$output_file" ]; then
    echo "Error: Input and output file names are identical. Please ensure input file ends with file extension '.svg' or manually specify an output file with '--outputfile'."
    exit
fi

# Delete frames in the temporary directory if they exist. Do not delete the directory itself.
# This is needed in case old frames are present from a previous run.
rm -f ./frames_tmp/frame_*.png


# Convert the animated SVG to a sequence of PNG frames
node anim_svg_to_png_frames.js --numframes $numframes --delay $delay --svgfile "$input_file" --outputdir "./frames_tmp"
./png_frames_to_apng.bash --framerate $framerate --outputfile "${output_file}" --inputdir "./frames_tmp"



