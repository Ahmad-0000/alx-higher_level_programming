#!/usr/bin/node

const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c = undefined) {
    if (!this.width || !this.height) {
      return;
    }
    let row = '';
    if (c && typeof c === 'string') {
      for (let i = 0; i < this.width; i++) {
        row += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        row += 'X';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
}

module.exports = Square;
