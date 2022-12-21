#!/usr/bin/python3
"""Daclares a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a square

            Args:
                size: size of square

        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square
        
            Return:
                Area of the square
        """
        return self._Square__size ** 2

    def my_print(self):
        """prints a square with # characters"""
        for i in range(self._Square__size):
            for j in range(self._Square__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
