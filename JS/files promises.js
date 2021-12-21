const fs = require('fs').promises;

// https://www.digitalocean.com/community/tutorials/how-to-work-with-files-using-the-fs-module-in-node-js

async function readFile(filePath) {
    try {
        const data = await fs.readFile(filePath);
        console.log(data.toString());
    } catch (error) {
        console.error(`Got an error trying to read the file: ${error.message}`);
    }
}

readFile(__dirname + '\\hello.txt');
