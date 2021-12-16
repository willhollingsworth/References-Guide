const fs = require('fs');
const path = require('path');

const short_folder = 'test_files';
const folder = path.join(__dirname, short_folder);

const short_file = 'test.txt';
const file = path.join(__dirname, short_folder, short_file);

const content = 'hello world!';
const append_data = 'super hello world!';

/*
crash course vid https://www.youtube.com/watch?v=fBNz5xF-Kx4
code https://github.com/bradtraversy/node_crash_course/tree/master/reference
*/

// // Create folder
function create_folder() {
    if (!fs.existsSync(folder)) {
        fs.mkdir(folder, {}, (err) => {
            if (err) throw err;
            console.log(short_folder, 'folder created');
        });
    } else {
        console.log(short_folder, 'folder already exists');
    }
}

// Create and write to file
function write_file() {
    if (!fs.existsSync(file)) {
        fs.writeFile(file, content, (err) => {
            if (err) throw err;
            console.log(short_file, 'created and written to');
        });
    } else {
        console.log(short_file, 'already exists');
    }
}

// File append
function append_file() {
    fs.appendFile(file, append_data, (err) => {
        if (err) throw err;
        console.log(short_file, 'appended to');
    });
}

// Read file
function read_file() {
    fs.readFile(file, 'utf8', (err, data) => {
        if (err) throw err;
        console.log(short_file, 'contains', data);
    });
}

// del file
function del_file() {
    if (fs.existsSync(file)) {
        fs.unlink(file, (err) => {
            if (err) throw err;
            console.log(short_file, 'deleted');
        });
    } else {
        console.log(short_file, "can't be deleted");
    }
}

// del folder
function del_folder() {
    if (fs.existsSync(folder)) {
        fs.rmdir(folder, {}, (err) => {
            console.log(short_folder, 'folder deleted...');
            if (err) throw err;
        });
    } else {
        console.log(short_folder, "folder doesn't exists");
    }
}

// async await functionality required otherwise it's done out of order
// better method would be using the newer promise based fs functionality
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
(async () => {
    create_folder();
    await sleep(20);
    write_file();
    await sleep(20);
    append_file();
    await sleep(20);
    read_file();
    await sleep(50);
    del_file();
    await sleep(20);
    del_folder();
})();

// create_folder().then((result) => write_file(result));
// .then(append_file()).then(read_file());
// .then(del_file());
// del_folder();
