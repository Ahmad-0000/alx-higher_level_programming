#!/usr/bin/node

const request = require('request');
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const argv = process.argv;
let result = 0;
let url = 0;

if (argv[2]) {
  const filmsUrl = argv[2];
  request(filmsUrl, function (error, response, body) {
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
}
