#!/usr/bin/python3
"""
Send a POST request with a JSON body containing a
dictionary with a key of 'q' , a value taken from the command-line arguments
"""
from requests import post
from sys import argv


def main():
    value = ""
    if len(argv) > 1:
        value = argv[1]

    dict_q = {"q": value}
    response = post("http://0.0.0.0:5000/search_user", data=dict_q)

    try:
        data = response.json()
        if len(data) == 0:
            print("No result")
        else:
            id_data = data.get('id')
            name = data.get('name')
            print("[{}] {}".format(id_data, name))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
