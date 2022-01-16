// https://stackabuse.com/building-a-rest-api-with-node-and-express/
// https://github.com/jkasun/simple-rest-sever-express
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const port = 5550;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.send('index is here');
});

app.post('/api', (req, res) => {
    const data = req.body;
    console.log(data);
    res.send(data);
    res.end();
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});
