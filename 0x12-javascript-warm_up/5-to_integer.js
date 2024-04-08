#!/usr/bin/node

const argv = process.argv;

if (argv[2]) {
  if (typeof +argv[2] === 'number') {
    const number = +argv[2];
    console.log(`My number: Math.floor(number)`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
