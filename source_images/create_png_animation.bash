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


#!/bin/bash

colors=("gray" "green" "orange" "purple" "yellow")

# Function to generate HTML
generate_html() {
    local colors=("$@")
    local output_file="${output_dir}/index.html"

    echo "<!DOCTYPE html>" > "$output_file"
    echo "<html>" >> "$output_file"
    echo "<head>" >> "$output_file"
    echo "    <title>Bird Images</title>" >> "$output_file"
    echo "</head>" >> "$output_file"
    echo "<body>" >> "$output_file"

    for color in "${colors[@]}"; do
        filename="bird${color}_animated.png"
        echo "    <img src=\"$filename\" alt=\"$color bird\"><br>" >> "$output_file"
    done

    echo "</body>" >> "$output_file"
    echo "</html>" >> "$output_file"

    echo "HTML file '$output_file' generated successfully."
}

# Convert frames to animated images
for color in "${colors[@]}"; do
    # Created animated 'singing' birds
    output_file_singing="${output_dir}/bird${color}_singing.png"
    echo "Converting ${color} bird frames to ${output_file_singing}"
    ffmpeg -y -framerate 2 -i "bird${color}_frame%d.png" -plays 0 -vf "fps=2" -f apng "${output_file_singing}"

    # Create non-animated 'sitting' birds by simply copying the first frame
    output_file_sitting="${output_dir}/bird${color}_sitting.png"
    echo "Copying first frame to ${output_file_sitting}"
    cp "bird${color}_frame1.png" "${output_file_sitting}"
done

# Generate HTML with the colors
generate_html "${colors[@]}"


echo "Script done. Check output above for any errors."

