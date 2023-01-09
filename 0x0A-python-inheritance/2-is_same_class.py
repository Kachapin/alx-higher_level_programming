#!/usr/bin/python3
"""Defines function to check class"""


def is_same_class(obj, a_class):
    """Checks if an object is of a class"""
    if type(obj) == a_class:
        return True
    return False
    