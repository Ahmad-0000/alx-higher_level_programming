#!/usr/bin/node

exports.converter = function (base) {
  function inner (arg) {
    return +arg.toString(base);
  }
  return inner;
};
