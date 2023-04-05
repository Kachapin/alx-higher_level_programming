#!/usr/bin/python3
"""module that opens url"""
from urllib.request import urlopen
from sys import argv


def main():
    """Opens url and reads data
    """
    with urlopen(argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == '__main__':
    """prevent execution on import"""
    main()
