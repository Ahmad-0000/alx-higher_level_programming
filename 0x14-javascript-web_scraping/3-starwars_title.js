#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

if (typeof +id === 'number') {
  request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const jsonData = JSON.parse(body);
      console.log(jsonData.title);
    }
  });
}
