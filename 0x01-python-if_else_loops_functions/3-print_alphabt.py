#!/usr/bin/python3
num = 97
while num < 123:
    if num == 101 or num == 113:
        num = num + 1
        continue
    print("{}".format(chr(num)), end="")
    num = num + 1
    