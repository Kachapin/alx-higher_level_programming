#!/usr/bin/python3
"""Defines class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns width/ height"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Updates attributes"""
        i = 0
        if args and len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary of attributes"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        