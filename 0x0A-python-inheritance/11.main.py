#!/usr/bin/python3
"""Defines square rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return area"""
        return self.__size ** 2

    def __str__(self):
        """Represent string method."""
        return "[Square] " + \
            str(self.__size) + "/" + str(self.__size)
            