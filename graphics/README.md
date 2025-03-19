# Graphics -- Creating an animated PNG image from an animated PNG

This is a small node script that generates PNG frames from an animated PNG. Then, ffmpeg is used to then encodes these frames to a animated PNG (APNG) file.

Overall, it converts an animated SVG to an APNG.

This can be used under Linux, and with some extra effort under Windows (if you have a proper shell like the MINGW bash that comes with Git for Windows).

## Installation

* Make sure you have `npm` installed, if not get the LTS from the [node website](https://nodejs.org/) or from your package manager. I used v10.9.2.
* Make sure you have `ffmpeg` installed and on your PATH. Under Linux you most likely already have it, otherwise install from your package manager. Under Windows you could use chocolate to install it, or manually install a Windows build from the ffmpeg website.
* Install dependencies. In this directory: ```npm ci```

## Usage

Name the SVG file you want to convert robot.svg and embed the JS function from the example robot.svg file at the top. Your SVG should start like this:

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
* Run ffmpeg script: ```./png_frames_to_apng.bash```         # Combines PNG frames into a single APNG

You may want to adapt the framerate in the ffmpeg script.

The ffmpeg script creates a file named `animated.png`. Make sure to view this APNG file in a suitable application, like Firefox or Chrome. Software like MS Paint will not display the animation.
