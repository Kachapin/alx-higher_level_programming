#!/usr/bin/node
const arr = require('./100-data.js').list;
console.log(arr);
const arr2 = arr.map((element, index) => element * index);
console.log(arr2);
