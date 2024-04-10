#!/usr/bin/node

exports.convertor = function (base) {
  function inner (arg) {
    return +arg.toString(base);
  }
  return inner;
};
