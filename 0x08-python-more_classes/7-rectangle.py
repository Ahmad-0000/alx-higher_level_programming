#!/usr/bin/python3
"""
A module containing one class "Rectangle"
"""


class Rectangle:
    """
    A class with width and height attribures.

    It contains perimeter and area methods.

    The method __str__ is modified to print
    a string represntation of the rectangle.

    The method __repr__ is modified to return
    a string representation that can be used
    to recreate an object using eval().

    "number_of_instances" is a class public
    attribute to track the number of objects
    (Rectangles) created

    "print_symbol" is a class public attribute
    to determine the symbol used to print the
    rectangle representation using __str__
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        str_rep = ""
        if self.__width == 0 or self.__height == 0:
            return str_rep
        ps = self.__dict__.get("print_symbol", None)
        if not ps:
            ps = Rectangle.print_symbol
        ps = str(ps)
        for i in range(self.__width):
            str_rep += ps
        row = str_rep
        str_rep = ''
        for j in range(self.__height):
            str_rep += row + '\n'
        return str_rep[:-1]

    def __repr__(self):
        return str(self)

    def __del__(self):
        print("Deleted a rectangle...")
        Rectangle.number_of_instances -= 1
