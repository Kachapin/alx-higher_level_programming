#!/usr/bin/python3
"""
Module containing a function to print a square with the character #.
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
    size: The size (length) of the square. Must be an integer.
    
    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
