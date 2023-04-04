#!/usr/bin/python3

"""
Module that sends a POST request to a given URL
with an email as a parameter and prints the
decoded body of the response.
"""

from requests import post
from sys import argv


def main():
    """Encodes email and sends POST request"""
    url = argv[1]
    email = argv[2]

    email_data = {"email": email}

    response = post(url, data=email_data)
    body_response = response.text
    print(body_response)


if __name__ == "__main__":
    main()
