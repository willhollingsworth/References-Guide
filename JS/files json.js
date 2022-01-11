const fs = require('fs');
const path = require('path');

const file_path = path.join(__dirname, 'hello.json');

const file = fs.readFileSync(file_path, 'utf8', (err, data) => {
    return data;
});

console.log(JSON.parse(file));
