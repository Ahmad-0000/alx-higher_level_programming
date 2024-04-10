#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
console.log(list.map(function (x) {
  let currentIndex = -1;
  function inner (x) {
    return ++currentIndex * x;
  }
  return inner;
}()));
