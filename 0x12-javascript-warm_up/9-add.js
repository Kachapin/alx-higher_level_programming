#!/usr/bin/node
const argv = process.argv;
const add = (a, b) => a + b;

console.log(add(+argv[2], +argv[3]));
