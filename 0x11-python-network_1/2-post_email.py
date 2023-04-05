#!/usr/bin/python3
"""sends post request to URL"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


def main():
    """encodes email and sends post request"""
    url = argv[1]
    email = argv[2]

    email_encode = urlencode({"email": email}).encode('utf-8')

    with urlopen(url, email_encode) as response:
        body_response = response.read().decode('utf-8')
        print(body_response)


if __name__ == "__main__":
    main()
