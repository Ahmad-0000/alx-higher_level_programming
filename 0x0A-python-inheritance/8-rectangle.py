#!/usr/bin/python3
"""
A module containg an empty class:
    "Rectangle"
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from "BaseGeometry" class
    """

    def __init__(self, width, height):
        """
        Initialization function
        """

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
