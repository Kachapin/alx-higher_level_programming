#!/usr/bin/python3
"""Reads file contents"""


def read_file(filename=""):
    """prints contente of file"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
        f.closed
        