#!/usr/bin/node
const argv = process.argv;
const count = argv[2];

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  while (parseInt(argv[2]) > 0) {
    console.log(`${'X'.repeat(count)}`);
    argv[2]--;
  }
}
