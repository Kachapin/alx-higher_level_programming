#!/usr/bin/node
const dict = require('./101-data.js').dict;
const output = {};

for (const [key, value] of Object.entries(dict)) {
  if (output[value] === undefined) {
    output[value] = [];
  }
  output[value].push(key);
}
console.log(output);
