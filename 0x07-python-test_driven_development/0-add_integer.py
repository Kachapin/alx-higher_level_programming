#!/usr/bin/python3
"""
Define a function to add two integers

Returns addition of the two integers
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float."""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
        