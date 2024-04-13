#!/usr/bin/python3
"""A module containing one class:
    "Rectangle"
This class inherits from the class
"Base" to reduce code repetition.
Rectangle class will have a lot of
functionality later on
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    My "Square" class that inherites
    from "Rectangle" class from the
    "rectangle" module, thus, using
    rectangle with square class is
    possible
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initilaization method that uses "super" function
        to intialize size, x and y using "rectangle" class
        initialization method
        """
        super().__init__(size, size, x, y)

    def __str__(self):
        """
        Customized "__str__" method to retrive a string
        represntation of the instance when using "print"
        or "str" functions
        """
        return f'[Square] ({self.id}) {self._Rectangle__x}/\
{self._Rectangle__y} - {self._Rectangle__width}'

    @property
    def size(self):
        """
        A property to retrive "size" attribute
        """
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """
        A setter to set "size" attribute
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self._Rectangle__width = value
        self._Rectangle__height = value
