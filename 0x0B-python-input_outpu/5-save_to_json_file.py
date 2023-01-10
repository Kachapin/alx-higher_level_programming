#!/usr/bin/python3
"""Save JSON string to file"""
import json


def save_to_json_file(my_obj, filename):
    """Save JSON to file"""

    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
        