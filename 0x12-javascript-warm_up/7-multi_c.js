#!/usr/bin/node
const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (parseInt(argv[2]) > 0) {
    console.log('C is fun');
    argv[2]--;
  }
}
