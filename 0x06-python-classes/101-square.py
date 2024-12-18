#!/usr/bin/python3
""" A Square module """


class Square:
    """ A simple square with size validation and area method, but
    no privacy"""
    def __init__(self, size=0, position=(0, 0)):
        """ A constructor method """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ A getter method for retrieving position """
        return self.__position

    @position.setter
    def position(self, value):
        """ A setter method for setting position """
        if type(value) is not tuple or len(value) != 2\
                or type(value[0]) is not int or type(value[1]) is not int or\
                value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ A method for calculating the square area """
        return self.__size ** 2

    def my_print(self):
        """ A method for printing the square """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """Customizing string representation"""
        string = ''
        if not self.__size:
            return string
        else:
            for i in range(self.__position[1]):
                string += '\n'
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    string += " "
                for j in range(self.__size):
                    string += "#"
                string += "\n"
        return string[:-1]
