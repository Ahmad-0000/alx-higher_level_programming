#!/usr/bin/python3
""" A module containing one class:
    "Rectangle"
This class inherits from the class
"Base" to reduce code repetition.
Rectangle class will have a lot of
functionality later on """
from base import Base


class Rectangle(Base):
    """    My "Rectangle" class that inherites
    from "Base" class from the "base"
    module, thus, having the ability to
    initialize "id" instance attribute using
    "Base" initializer"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intialization method. "id" will be initalized using
        "base" class initializer, and the other attributes
        will be intialized using their own properties and
        setters
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """ 
        A property to retrive "width" to ensure "Encapsulation"
        principle, in this way, I prevent the users form messing
        with my class with their input
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A setter to set "width" to ensure "Encapsulations"
        principle, therer are some restrictions regarding
        the values that can be used to assign to the attribute
        width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        A property to reterive "height" to ensure "Encapsulation",
        in this way I can let the user see the content of the
        private property "__height" without letting him mess
        width my class implementation
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A setter to set "height" to ensure "Encapsulations"
        principle, so that there are some restrictions
        regarding usr input, so the wrong input will no
        affect the class
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        A property to reterive "x" to ensure "Encapsulation"
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        A setter to set "x" to ensure "Encapsulations"
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        A property to reterive "y" to ensure "Encapsulation"
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        A setter to set "y" to ensure "Encapsulations"
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        A public method to return the area of the "Rectanlge"
        instance
        """
        return self.__width * self.__height

    def display(self):
        """
        A public instance method to print a representation
        of the rectangle using "#" symbol
        """
        row = "#"
        for i in range(self.__width - 1):
            row += "#"
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            print(row)

    def __str__(self):
        """
        Modified to return a string represntation when
        used
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        A pulic instance method to update the attributes id,
        width, height, x and y
        """
        private_attrs = ['__id', '__width', '__height', '__x', '__y']
        i = 0
        if args:
            for j in args:
                if i == 5:
                    break
                elif i == 0:
                    self.__dict__[f'_Base{private_attrs[i]}'] = args[i]
                else:
                    self.__dict__[f'_Rectangle{private_attrs[i]}'] = args[i]
                i += 1
        elif kwargs:
            keys = kwargs.keys()
            for key in keys:
                if i == 5:
                    break
                if key == 'id':
                    self.__dict__['_Base__id'] = kwargs['id']
                else:
                    self.__dict__[f'_Rectangle__{key}'] = kwargs[f'{key}']
                i += 1

    def to_dictionary(self):
        """
        A method to return a dicitonary representation
        of a "Rectangle" instance
        """
        dict_repr = {}
        dict_repr['x'] = self.x
        dict_repr['y'] = self.y
        dict_repr['id'] = self.id
        dict_repr['height'] = self.height
        dict_repr['width'] = self.width
        return dict_repr
