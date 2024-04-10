#!/usr/bin/node

exports.logMe = (function (item) {
  let itemIndex = 0;
  function inner (item) {
    if (item) {
      console.log(`${itemIndex}: ${item}`);
      itemIndex++;
    }
  }
  return inner;
}());
