#!/usr/bin/python3
"""Adds all arguments to list"""


if __name__ == "__main__":
    from sys import argv
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    data = []
    try:
        data = load_from_json_file("add_items.json")
        for item in argv[1:]:
            data.append(item)
        save_to_json_file(data, "add_item.json")
    except FileNotFoundError:
        for item in argv[1:]:
            data.append(item)
        save_to_json_file(data, "add_item.json")
        