#!/usr/bin/node

const argv = process.argv;

const size = +argv[2];
let row = '';
if (typeof size === 'number' && !isNaN(size)) {
  for (let i = 0; i < size; i++) {
    row += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
