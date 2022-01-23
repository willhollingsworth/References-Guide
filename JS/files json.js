const fs = require('fs');
const path = require('path');

const file_path = path.join(__dirname, 'hello.json');

const await file = fs.readFile(file_path, 'utf8', (err, data) => {
    return data;
});

console.log(JSON.parse(file));
