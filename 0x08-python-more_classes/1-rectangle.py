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
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        """
        Retrieves the width of a Rectangle instance.

        :return: The width of the rectangle.
        """
        return self._width

    def set_width(self, value):
        """
        Sets the width of a Rectangle instance.

        :param value: The new width value.
        :raises TypeError: If the width is not an integer.
        :raises ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def get_height(self):
        """
        Retrieves the height of a Rectangle instance.

        :return: The height of the rectangle.
        """
        return self._height

    def set_height(self, value):
        """
        Sets the height of a Rectangle instance.

        :param value: The new height value.
        :raises TypeError: If the height is not an integer.
        :raises ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    width = property(get_width, set_width, doc="Width of the Rectangle")
    height = property(get_height, set_height, doc="Height of the Rectangle")
