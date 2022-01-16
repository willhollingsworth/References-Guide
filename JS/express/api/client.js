// https://stackoverflow.com/questions/64874484/js-referenceerror-fetch-is-not-defined
const fetch = require('node-fetch');

payload = {
    title: 'foo',
    body: 'bar',
    userId: 1,
};

fetch('http://localhost:5550/api', {
    method: 'POST',
    body: JSON.stringify(payload),
    headers: { 'Content-type': 'application/json; charset=UTF-8' },
})
    .then((res) => res.json())
    .then((json) => console.log(json))
    .catch((err) => console.log(err));
