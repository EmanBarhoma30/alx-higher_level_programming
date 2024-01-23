#!/usr/bin/python3

"""
Module: MagicClass
"""

import math


class MagicClass:
    """
    Class: MagicClass
    Description: Represent a circle.
    """

    def __init__(self, radius=0):
        """
        Constructor.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
