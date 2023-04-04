#!/usr/bin/python3
"""module that opens url"""
from urllib.request import urlopen


def main():
    """Opens url and reads data
    """
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()

    print('Body response:')
    print('\t- type:', type(data))
    print('\t- content:', data)
    print('\t- utf8 content:', data.decode('utf-8'))


if __name__ == '__main__':
    """prevent execution on import"""
    main()
