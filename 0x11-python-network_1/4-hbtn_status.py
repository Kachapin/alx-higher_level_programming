#!/usr/bin/python3
"""fetches url response data"""
import requests


def main():
    """Opens url and reads data
    """
    response = requests.get('https://alx-intranet.hbtn.io/status')
    data = response.content.decode()

    print('Body response:')
    print('\t- type:', type(data))
    print('\t- content:', data)


if __name__ == '__main__':
    """prevent execution on import"""
    main()
