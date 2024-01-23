#!/usr/bin/python3

class Square:
    """
    Class: Square
    Description: Represents a square.
    """

    def __init__(self, size=0):
        """
        Constructor.

        Args:
            size (int): Length of the side of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
