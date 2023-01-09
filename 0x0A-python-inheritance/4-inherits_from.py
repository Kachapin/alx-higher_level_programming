#!/usr/bin/python3
"""Defines function to compare classes"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    Arguments:
        obj: object
        a_class: class object
    Returns:
        True or False
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
    