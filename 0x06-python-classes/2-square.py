#!/usr/bin/python3
""" This is the 3d task solution in today's project """


class Square:
    """ A simple square with size validation """
    def __init__(self, size=0):
        """ A constructor method """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
