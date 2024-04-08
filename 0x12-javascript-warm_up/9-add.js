#!/usr/bin/node

const argv = process.argv;
const firstNum = +argv[2];
const secondNum = +argv[3];

function add (a, b) {
  console.log(a + b);
}

add(firstNum, secondNum);
