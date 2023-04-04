#!/usr/bin/python3
"""get user id data"""
from requests import get
from sys import argv


def main():
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]

    response = get(url, auth=(username, password))

    data = response.json()
    print(data["id"])


if __name__ == "__main__":
    main()
