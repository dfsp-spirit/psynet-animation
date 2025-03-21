// Capture frames from an SVG file and save them as PNG images
// Requires that the SVG file has an embedded Javascript section with a function to advance the animation.
// This looks like this in the SVG header:
//
//<svg width="800" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
//    <script type="application/ecmascript">
//        <![CDATA[
//        function stepAnimation() {
//            document.documentElement.setCurrentTime(document.documentElement.getCurrentTime() + 1/30);
//        }
//        ]]>
//    </script>
//  more SVG content here
//

const puppeteer = require('puppeteer');
const path = require('path'); // Add the path module for cross-platform file paths
const fs = require('fs');

// Default values
let num_frames = 30;
let delay = 100;
let svgFile = 'file://' + path.join(__dirname, 'robot.svg');
let outputDir = path.join(__dirname, 'frames_tmp');

// Parse command-line arguments
process.argv.forEach((arg, index) => {
    if (arg === '--num_frames' && process.argv[index + 1]) {
        num_frames = parseInt(process.argv[index + 1], 10);
    } else if (arg === '--delay' && process.argv[index + 1]) {
        delay = parseInt(process.argv[index + 1], 10);
    } else if (arg === '--svgFile' && process.argv[index + 1]) {
        svgFile = 'file://' + path.join(__dirname, process.argv[index + 1]);
    } else if (arg === '--outputDir' && process.argv[index + 1]) {
        outputDir = path.join(__dirname, process.argv[index + 1]);
    } else if (arg === '--help' || arg === '-h') {
        console.log('Usage: node anim_svg_to_png_frames.js [--num_frames <num_frames>] [--delay <delay>] [--svgFile <svgFile>] [--outputDir <outputDir>]');
        console.log('  --num_frames: Number of frames to capture (default: 30)');
        console.log('  --delay: Delay between frames in milliseconds (default: 100)');
        console.log('  --svgFile: SVG file to capture frames from, relative to current dir (default: robot.svg)');
        console.log('  --outputDir: Directory to save PNG frames to, relative to current dir (default: current dir). Must exist and be writable.');
        console.log('  --help, -h: Show this help message');
        console.log('Example: node anim_svg_to_png_frames.js --num_frames 20 --delay 120 --svgFile robot_anim_in.svg --outputDir frames');
        process.exit(0);
    }
});

// Check if SVG file exists
if (!fs.existsSync(svgFile.replace('file://', ''))) {
    console.error(`Error: SVG file "${svgFile}" not found.`);
    process.exit(1); // Exit with an error code
}

// Check if output directory exists
if (!fs.existsSync(outputDir)) {
    console.error(`Error: Output dir "${outputDir}" not found.`);
    process.exit(1); // Exit with an error code
}

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto(svgFile);

    // Set viewport size based on SVG dimensions to avoid extra whitespace
    const svgSize = await page.evaluate(() => {
        const svg = document.querySelector('svg');
        return { width: svg.width.baseVal.value, height: svg.height.baseVal.value };
    });
    await page.setViewport({ width: svgSize.width, height: svgSize.height });

    console.log('Capturing', num_frames, 'Frames with delay of', delay, 'ms.');
    console.log('SVG file:', svgFile);
    console.log('Output directory:', outputDir);
    console.log('SVG dimensions (and viewport size):', svgSize.width, 'x', svgSize.height);

    for (let i = 0; i < num_frames; i++) {
        let outputFilename = path.join(outputDir, `frame_${i.toString().padStart(3, '0')}.png`);
        await page.screenshot({ path: outputFilename, omitBackground: true });
        await page.evaluate(() => new Promise(requestAnimationFrame)); // Advance one frame
        await new Promise(resolve => setTimeout(resolve, delay));
        console.log('* ' + (i+1) + ' frames captured, writing generated image to ' + outputFilename);
    }

    await browser.close();
    console.log('All', num_frames, 'Frames captured!');
})();