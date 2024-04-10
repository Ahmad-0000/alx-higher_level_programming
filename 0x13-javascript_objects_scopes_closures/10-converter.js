#!/usr/bin/node

exports.converter = function (base) {
  function inner (arg) {
    if (isNaN(base) === true || isNaN(arg) === true) {
      return 0;
    }
    if (typeof base === 'number' && typeof arg === 'number') {
      if (base === 2 || base === 8 || base === 10 || base === 16) {
        return arg.toString(base);
      } else {
        return 0;
      }
    } else {
      return 0;
    }
  }
  return inner;
};
