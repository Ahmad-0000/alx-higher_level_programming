#!/usr/bin/node

const argv = process.argv;
const num = +argv[2];

function factorial (num) {
  function rec (num) {
    if (isNaN(num) || num === 0) {
      return 1;
    } else {
      return num * rec(num - 1);
    }
  }
  const factNum = rec(num);
  console.log(factNum);
}

factorial(num);
