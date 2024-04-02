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

    "bigger_or_equal" is a "staticmethod" to
    compare two "Rectangle" instances based on
    area. It returns the bigger, and if they
    have the same area, "rect_1" is returned
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0, print_symbol="#"):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = print_symbol

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
        Rectangle.print_symbol = str(self.print_symbol)
        for i in range(self.__width):
            str_rep = str_rep + Rectangle.print_symbol
        row = str_rep
        for j in range(self.__height):
            str_rep = str_rep + '\n' + row
        return str_rep

    def __repr__(self):
        return str(self)

    def __del__(self):
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
