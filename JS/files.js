const fs = require('fs');
const path = require('path');

const short_folder = 'test_files';
const folder = path.join(__dirname, short_folder);

const short_file = 'test.txt';
const file = path.join(__dirname, short_folder, short_file);

/*
crash course vid https://www.youtube.com/watch?v=fBNz5xF-Kx4
code https://github.com/bradtraversy/node_crash_course/tree/master/reference
*/

// // Create folder
if (!fs.existsSync(folder)) {
    fs.mkdir(folder, {}, (err) => {
        if (err) throw err;
        console.log('Folder created...');
    });
} else {
    console.log('folder already exists');
}
// Create and write to file
const content = 'hello world!';
if (!fs.existsSync(file)) {
    fs.writeFile(file, content, (err) => {
        if (err) throw err;
        console.log('File created and written to');
    });
} else {
    console.log('file already exists');
}

// File append
const append_data = 'super hello world!';
fs.appendFile(file, append_data, (err) => {
    if (err) throw err;
    console.log('data append to', short_file);
});

// // Read file
// fs.readFile(path.join(__dirname, folder, file), 'utf8', (err, data) => {
//     if (err) throw err;
//     console.log('reading file', data);
// });

// del file
if (!fs.existsSync(folder)) {
    fs.delete(folder, {}, (err) => {
        if (err) throw err;
        console.log('Folder deleted...');
    });
} else {
    console.log("folder doesn't exists");
}
