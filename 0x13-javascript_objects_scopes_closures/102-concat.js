#!/usr/bin/node
const argv = process.argv;
a = fopen(argv[2], 0);
contentA = fread(a,flength(a));
b = fopen(argv[3], 0);
contentB = fread(b,flength(b));

c = fopen(argv[4], 3);
fwrite(c, contentA);
fwrite(c, contentB);
