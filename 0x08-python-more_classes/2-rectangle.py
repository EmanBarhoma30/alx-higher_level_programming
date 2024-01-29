#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        :param width: The width of the new rectangle.
        :param height: The height of the new rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Retrieve the width of the Rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        :param value: The new width value.
        :raises TypeError: If the width is not an integer.
        :raises ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Retrieve the height of the Rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        :param value: The new height value.
        :raises TypeError: If the height is not an integer.
        :raises ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Return the area of the Rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Return the perimeter of the Rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
