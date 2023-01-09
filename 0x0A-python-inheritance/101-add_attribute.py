#!/usr/bin/python3
"""Defines function to add attribute"""


def add_attribute(obj, attr, value):
    """adds new attribute if possible"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
    