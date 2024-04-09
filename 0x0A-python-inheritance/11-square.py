#!/usr/bin/python3
"""
A module containing one class:
    "Square"
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class
    """

    def __init__(self, size):
        """
        Initialization method
        """

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        A method to return a string representation
        of a square object
        """

        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        A method to return the area of a square
        object
        """

        return self.__size ** 2
