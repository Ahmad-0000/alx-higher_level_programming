#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
let resultContent = '';

try {
  const file1Content = fs.readFileSync(file1, 'utf8');
  const file2Content = fs.readFileSync(file2, 'utf8');
  resultContent = `${file1Content}${file2Content}`;
  fs.writeFileSync(file3, resultContent);
} catch (error) {
  console.error(error);
}
