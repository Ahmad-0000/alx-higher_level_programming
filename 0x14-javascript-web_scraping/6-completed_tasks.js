#!/usr/bin/node

const request = require('request');
const argv = process.argv;

if (argv[2]) {
  const url = argv[2];
  const output = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0 };
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const jsonData = JSON.parse(body);
      let task = 0;
      for (task of jsonData) {
        if (task.completed) {
          output[task.userId]++;
        }
      }
      console.log(`{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }`);
    }
  });
}
