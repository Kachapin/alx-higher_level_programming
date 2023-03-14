#!/usr/bin/node
const argv = process.argv;
function factorial (num) {
  if (num !== 1) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}
argv[2] = isNaN(argv[2]) ? 1 : argv[2];
console.log(factorial(+argv[2]));
