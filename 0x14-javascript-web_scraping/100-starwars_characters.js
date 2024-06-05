#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

if (typeof +id === 'number') {
  request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const filmInfo = JSON.parse(body);
      const characters = filmInfo.characters;
      let key = 0;
      for (key of characters) {
        request(key, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      }
    }
  });
}
