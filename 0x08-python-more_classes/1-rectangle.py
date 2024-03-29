#!/usr/bin/python3
"""
Define a class that is called Rectangle
"""


class Rectangle:
    """Rectangle : width and height"""

    def __init__(self, width=0, height=0):
        """initializes a Rectangle instanc
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width of a Rectangle instanc"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of a Rectangle instanc
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
