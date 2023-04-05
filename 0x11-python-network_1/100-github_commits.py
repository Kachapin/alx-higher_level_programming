#!/usr/bin/python3
"""get user id data"""
from requests import get
from sys import argv


def main():
    repo = argv[1]
    user = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    response = get(url)

    data = response.json()
    i = 0
    for commit in data:
        print("{}: {}".format(commit['sha'],
                              commit['commit']['author']['name']))
        i += 1
        if i == 10:
            break


if __name__ == "__main__":
    main()
