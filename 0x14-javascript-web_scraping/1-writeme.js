#!/usr/bin/node

const fs = require('fs').promises;
const argv = process.argv;
const filePath = argv[2];
const content = argv[3];

async function writingFile (filePath, content) {
  try {
    await fs.writeFile(filePath, content);
  } catch (error) {
    console.log(error.message);
  }
}

writingFile(filePath, content);
