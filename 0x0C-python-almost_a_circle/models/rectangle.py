#!/usr/bin/python3
"""A module containing one class:
    "Rectangle"
This class inherits from the class
"Base" to reduce code repetition.
Rectangle class will have a lot of
functionality later on
"""
from base import Base


class Rectangle(Base):
    """
    My "Rectangle" class that inherites
    from "Base" class from the "base"
    module, thus, having the ability to
    initialize "id" instance attribute using
    "Base" initializer
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intialization method to intialize these attributes:
            width
            height
            x
            y
        "id" will be initalized using "base" class initializer
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        A property to reterive "width"
        to ensure "Encapsulation"
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A setter to set "width"
        to ensure "Encapsulations"
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        A property to reterive "height"
        to ensure "Encapsulation"
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A setter to set "height"
        to ensure "Encapsulations"
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        A property to reterive "x"
        to ensure "Encapsulation"
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        A setter to set "x"
        to ensure "Encapsulations"
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        A property to reterive "y"
        to ensure "Encapsulation"
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        A setter to set "y"
        to ensure "Encapsulations"
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
