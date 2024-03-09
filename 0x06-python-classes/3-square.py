#!/usr/bin/python3
""" The 4th task solution of today's project """


class Square:
    """ A simple square with size validation and area method"""
    def __init__(self, size=0):
        """ A constructor method """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ A method to calculate the are of the square """
        return self.__size ** 2
