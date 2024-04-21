#!/usr/bin/python3
'''     A module containing one class:
    "Rectangle"
This class inherits from the class
"Base" to reduce code repetition.
Rectangle class will have a lot of
functionality later on '''
from models.base import Base


class Rectangle(Base):
    '''    My "Rectangle" class that inherites
    from "Base" class from the "base"
    module, thus, having the ability to
    initialize "id" instance attribute using
    "Base" initializer'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''        Intialization method. "id" will be initalized using
        "base" class initializer, and the other attributes
        will be intialized using their own properties and
        setters'''
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        '''         A property to retrive "width" to ensure "Encapsulation"
        principle, in this way, I prevent the users form messing
        with my class with their input'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''        A property to reterive "height" to ensure "Encapsulation",
        in this way I can let the user see the content of the
        private property "__height" without letting him mess
        width my class implementation'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''        A property to retrive "x" to ensure "Encapsulation"
        principle so that the user can acess the private
        attribute '__x' without messing with the class'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''        A property to reterive "y" to ensure "Encapsulation"
        principle, so that the user can access the private
        attribute "__y" without messing with the class'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''
        A public method to return the area of the "Rectanlge"
        instance
        '''
        return self.__width * self.__height

    def display(self):
        '''
        A public instance method to print a representation
        of the rectangle using "#" symbol
        '''
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
        '''
        Modified to return a string represntation when
        used
        '''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        '''
        A pulic instance method to update the attributes id,
        width, height, x and y
        '''
        if args:
            l = []
            for i in args:
                l.append(i)
            l = tuple(l)
            if len(args) == 1:
                self.id = l[0]
            elif len(args) == 2:
                self.id, self.width = l
            elif len(args) == 3:
                self.id, self.width, self.height = l
            elif len(args) == 4:
                self.id, self.width, self.height, self.x = l
            elif len(args) >= 5:
                self.id, self.width, self.height, self.x, self.y = l
        elif kwargs:
            keys = kwargs.keys()
            for key in keys():
                if key == 'id':
                    self.id = kwargs['id']
                elif key == 'width':
                    self.width = kwargs['width']
                elif key == 'height':
                    self.height = kwargs['height']
                elif key == 'x':
                    self.x = kewargs['x']
                elif key == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        '''
        A method to return a dicitonary representation
        of a "Rectangle" instance
        '''
        dict_repr = {}
        dict_repr['x'] = self.x
        dict_repr['y'] = self.y
        dict_repr['id'] = self.id
        dict_repr['height'] = self.height
        dict_repr['width'] = self.width
        return dict_repr
