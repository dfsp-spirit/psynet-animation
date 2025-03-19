# Graphics -- Creating an animated PNG image from an animated PNG

This is a small node script that generates PNG frames from an animated PNG. Then, ffmpeg is used to then encodes these frames to a animated PNG (APNG) file.

Overall, it converts an animated SVG to an APNG.

## Installation

* Make sure you have npm installed, if not get the LTS from the [node website](https://nodejs.org/)
* Install dependencies: ```npm ci```
* Run the first script: ```node anim_svg_to_apng.js``` # Generates the frames
* Run ffmpeg

Usage