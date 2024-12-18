#!/usr/bin/python3
"""
A module containing one class "Rectangle"
"""


class Rectangle:
    """
    A rectangle class with width and height
    attributes and area, perimenter mthods.
    The __str__ method is modified to print
    a representation of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """A string representation for the end user
        """
        str_rep = ""
        if self.__width == 0 or self.__height == 0:
            return str_rep
        for i in range(self.__width):
            str_rep = str_rep + "#"
        row = str_rep
        for j in range(self.__height - 1):
            str_rep = str_rep + '\n' + row
        return str_rep

    def __repr__(self):
        """A string represenation to used by 'eval'
        """
        return f'Rectangle({self.width}, {self.height})'
