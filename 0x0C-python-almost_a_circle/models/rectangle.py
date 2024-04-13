#!/usr/bin/python3
"""
A module containing one class:
    "Rectangle"
"""
from base import Base


class Rectangle(Base):
    """
    My "Rectangle" class that inherites from "Base" class from the
    "base" module
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intialization method
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        A property to reterive "width"  to ensure "Encapsulation"
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A setter to set "width" to ensure "Encapsulations"
        """
        self.__width = value

    @property
    def height(self):
        """
        A property to reterive "height"  to ensure "Encapsulation"
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A setter to set "height" to ensure "Encapsulations"
        """
        self.__height = value

    @property
    def x(self):
        """
        A property to reterive "x"  to ensure "Encapsulation"
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        A setter to set "x" to ensure "Encapsulations"
        """
        self.__x = value

    @property
    def y(self):
        """
        A property to reterive "y"  to ensure "Encapsulation"
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        A setter to set "y" to ensure "Encapsulations"
        """
        self.__y = value
