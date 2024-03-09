#!/usr/bin/python3
""" The 5th task solution for today's project """


class Square:
    """ A simple square with size validation and area method, but
    no privacy"""
    def __init__(self, size=0):
        """ A constructor method """
        self.size = size

    @property
    def size(self):
        """ A getter method for retrieving size """
        return self.__size

    @size.setter
    def size(self, size):
        """ A setter method for setting size """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ A method for retrievning the are of the square """
        return self.__size ** 2
