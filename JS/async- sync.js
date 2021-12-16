function rand() {
    return Math.floor(Math.random() * 100);
}

// for (i = 0; i < 3; i++) {
//     r = rand();
//     setTimeout(() => {
//         console.log(i, r);
//     }, r);
// }

// forcing synchronous behavior
// https://www.sitepoint.com/delay-sleep-pause-wait/
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
async function delayedGreeting() {
    console.log('Hello');
    await sleep(200);
    console.log('World!');
    await sleep(200);
    console.log('Goodbye!');
}

delayedGreeting();
