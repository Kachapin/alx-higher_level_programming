#!/usr/bin/python3
"""Defines MyList class"""


class MyList(list):
    """Initialites the class"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
        