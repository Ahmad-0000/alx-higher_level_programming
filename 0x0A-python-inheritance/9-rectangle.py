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

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
