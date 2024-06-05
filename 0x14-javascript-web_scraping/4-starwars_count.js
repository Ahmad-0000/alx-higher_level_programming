#!/usr/bin/node

const request = require('request');
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let result = 0;
let url = 0;

request('https://swapi-api.alx-tools.com/api/films', function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const jsonData = JSON.parse(body);
    let count = 0;
    for (result of jsonData.results) {
      const characters = result.characters;
      for (url of characters) {
        if (url === characterUrl) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
