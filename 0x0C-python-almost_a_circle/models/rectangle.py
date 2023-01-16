#!/usr/bin/python3
"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Retangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Return value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def display(self):
        """Print rectangle"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Overides string method"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates attributes"""
        i = 0
        if args and len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """Return Dictionary"""
        dictionary = {"id": self.id, "width": self.width,
                      "height": self.height,
                      "x": self.x, "y": self.y}
        return dictionary
        