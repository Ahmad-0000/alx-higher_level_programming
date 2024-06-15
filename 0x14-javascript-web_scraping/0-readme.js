#!/usr/bin/node

const fs = require('fs').promises;
const argv = process.argv;
const filePath = argv[2];

async function readingFile (filePath) {
  const data = await fs.readFile(filePath);
  console.log(data.toString());
}

readingFile(filePath);
