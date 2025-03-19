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

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const svgFile = 'file://' + __dirname + '/robot.svg'; // Change to your SVG file path

    await page.goto(svgFile);

    const num_frames = 30; // Number of frames to capture
    const delay = 100; // Delay between frames in ms

    for (let i = 0; i < num_frames; i++) {
        await page.screenshot({ path: `frame_${i.toString().padStart(3, '0')}.png`, omitBackground: true });
        await page.evaluate(() => new Promise(requestAnimationFrame)); // Advance one frame
        await new Promise(resolve => setTimeout(resolve, delay)); // Fixed timeout function
    }

    await browser.close();
    console.log('Frames captured!');
})();
