#!/usr/bin/node

const argv = process.argv;

const argument = +argv[2];

if (typeof argument === 'number' && !isNaN(argument)) {
  for (let i = 0; i < argument; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
