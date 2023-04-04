#!/usr/bin/python3
"""module that opens url"""
from urllib.request import urlopen
from sys import argv
import urllib.error


def main():
    """Opens url and reads data
    """
    try:
        with urlopen(argv[1]) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    """prevent execution on import"""
    main()
