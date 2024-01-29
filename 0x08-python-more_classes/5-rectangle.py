#!/usr/bin/python3
"""
Define a class called Rectangle
"""


class Rectangle:
    """Rectangle: width and height"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return '\n'.join(['#' * self.__width for _ in range(self.__height)]) \
            if self.__height and self.__width else ''

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height and self.__width:
            return 2 * (self.__width + self.__height)
        else:
            return 0


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")
    print(str(my_rectangle))
