#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || h == null || w == null) {
      Object.create(null);
    } else {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
