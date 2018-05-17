#!/usr/bin/node
const fs = require('fs');
let firstFile = process.argv[2];
let secondFile = process.argv[3];
let toWrite = process.argv[4];
console.log(firstFile);
f1 = fs.openSync(firstFile, 'r', (err, fd));
fs.read(f1);

//console.log(data);
//if (f1 != -1) {
//  str1 = f1.read();
//  console.log(str);
//}
