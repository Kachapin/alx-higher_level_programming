#!/usr/bin/python3
"""Defines funtion that prints name"""


def say_my_name(first_name, last_name=""):
    """
    Print a message with a person's first and last name.

    Args:
    first_name: A string representing the person's first name.
    last_name: A string representing the person's last name (optional).
    
    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
