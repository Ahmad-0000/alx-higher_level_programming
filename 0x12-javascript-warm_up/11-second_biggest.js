#!/usr/bin/node

const argv = process.argv;

if (argv.length < 2) {
  console.log(0);
} else {
  let biggest = 0;
  let secondBiggest = 0;
  for (let i = 0; i < argv.length - 2; i++) {
    if (+argv[2 + i] > biggest) {
      biggest = +argv[2 + i];
    }
  }
  for (let i = 0; i < argv.length - 2; i++) {
    if (+argv[2 + i] > secondBiggest && +argv[2 + i] < biggest) {
      secondBiggest = +argv[2 + i];
    }
  }
  console.log(secondBiggest);
}
