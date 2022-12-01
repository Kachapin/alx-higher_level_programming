#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
if argc == 1:
    print("0 arguments.")
elif argc == 2:
    print("1 argument:")
    print("1: {}".format(argv[1]))
else:
    print("{:d} arguments:".format(argc - 1))
    for i in range(1, argc):
        print("{:d}: {}".format(i, argv[i]))
