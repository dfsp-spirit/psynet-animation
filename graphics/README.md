# Graphics -- Creating an animated PNG image from an animated SVG


The tools in this directory convert an animated SVG file to an animated PNG file.

This is a two-step process:

* First, a small node script that generates PNG frames from an animated SVG.
* Then, ffmpeg is used to encode these frames to a animated PNG (APNG) file.

This can be used under Linux, and with some extra effort under Windows (if you have a proper shell like the MINGW bash that comes with Git for Windows).

## Installation

* Make sure you have `npm` installed, if not get the LTS from the [node website](https://nodejs.org/) or from your package manager. I used v10.9.2.
* Make sure you have `ffmpeg` installed and on your PATH. Under Linux you most likely already have it, otherwise install from your package manager. Under Windows you could use chocolate to install it, or manually install a Windows build from the ffmpeg website.
* Install JavaScript dependencies via npm. In this directory: ```npm ci```

## Usage

Name the SVG file you want to convert `robot.svg` and embed the JS function from the example robot.svg file at the top. Your SVG should start like this:

```
<svg width="800" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
    <script type="application/ecmascript">
        <![CDATA[
        function stepAnimation() {
            document.documentElement.setCurrentTime(document.documentElement.getCurrentTime() + 1/30);
        }
        ]]>
    </script>
  // more SVG content here
```

* Run the first script: ```node anim_svg_to_png_frames.js``` # Generates the frames (set of non-animated PNG files)
* Run ffmpeg script: ```./png_frames_to_apng.bash```         # Combines all PNG frames into a single APNG
* Delete the frames to avoid potential issues next time you use the scripts: ```rm frame_*.png```

Note: You may want to adapt the output framerate. To do that, pass it as first command line argument, e.g.: ```./png_frames_to_apng.bash 5``` for five frames per second.

The ffmpeg script creates an output file named `animated.png`. Make sure to view this APNG file in a suitable application, like Firefox or Chrome. Software like MS Paint that does not support APNG will not display the animation, but only the first frame.
