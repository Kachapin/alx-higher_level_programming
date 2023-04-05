#!/usr/bin/python3

"""
Module that opens a URL and displays the decoded
body of the response. Handles HTTP errors and
displays the error code.
"""

from requests import get
from sys import argv


def main():
    """Opens URL and reads data"""
    url = argv[1]

    response = get(url)
    if response.status_code < 400:
        print(response.content.decode())
    else:
        print("Error code: {}".format(response.status_code))


if __name__ == '__main__':
    """Prevent execution on import"""
    main()
