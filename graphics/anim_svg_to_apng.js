const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const svgFile = 'file://' + __dirname + '/robot.svg'; // Change to your SVG file path

    await page.goto(svgFile);

    const frames = 30; // Number of frames to capture
    const delay = 100; // Delay between frames in ms

    for (let i = 0; i < frames; i++) {
        await page.screenshot({ path: `frame_${i.toString().padStart(3, '0')}.png`, omitBackground: true });
        await page.evaluate(() => new Promise(requestAnimationFrame)); // Advance one frame
        await new Promise(resolve => setTimeout(resolve, delay)); // Fixed timeout function
    }

    await browser.close();
    console.log('Frames captured!');
})();
