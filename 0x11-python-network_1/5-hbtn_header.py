#!/usr/bin/python3
"""gets request id"""
from requests import get
from sys import argv


def main():
    """Opens url and reads data
    """
    response = get(argv[1])
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == '__main__':
    """prevent execution on import"""
    main()
