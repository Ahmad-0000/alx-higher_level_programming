#!/usr/bin/node

const request = require('request');
const fs = require('fs').promises;
const argv = process.argv;

if (argv[3]) {
  const url = argv[2];
  const filePath = argv[3];
  request(url, async function (error, response, body) {
    if (!error && response.statusCode === 200) {
      await fs.writeFile(filePath, body);
    }
  });
}
