#!/usr/bin/node

const argv = process.argv;

if (argv[2]) {
	const argument = +argv[2];
  if (typeof argument === 'number' && isNaN(argument) === false) {
    console.log(`My number: ${Math.floor(argument)}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
