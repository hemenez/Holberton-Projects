#!/usr/bin/node
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
function add (a, b) {
  let c = a + b;
  console.log(c);
}
add(a, b);
