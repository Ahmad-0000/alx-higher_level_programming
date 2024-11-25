#!/usr/bin/python3
'''A module containing one class:
    "Rectangle"
This class inherits from the class
"Base" to reduce code repetition.
Rectangle class will have a lot of
functionality later on
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    My "Square" class that inherites
    from "Rectangle" class from the
    "rectangle" module, thus, using
    rectangle with square class is
    possible
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initilaization method that uses "super" function
        to intialize size, x and y using "rectangle" class
        initialization method
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Customized "__str__" method to retrive a string
        represntation of the instance when using "print"
        or "str" functions
        '''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        '''
        A property to retrive "size" attribute
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        A setter to set "size" attribute
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        A method to update id, size, x and y. if "args"
        is present and not empty, it will be used, otherwise
        "kwargs" will be used for updating
        '''
        length = len(args)
        if args:
            if length == 1:
                self.id = args[0]
            elif length == 2:
                self.id, self.size = args
            elif length == 3:
                self.id, self.size, self.x = args
            elif length >= 4:
                self.id, self.size, self.x, self.y = args
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs[f'{key}']
            if "size" in kwargs:
                self.size = kwargs[f'{key}']
            if "x" in kwargs:
                self.x = kwargs[f'{key}']
            if "y" in kwargs:
                self.y = kwargs[f'{key}']

    def to_dictionary(self):
        '''
        A method to retrieve a dictionary representation
        of a "Square" instance
        '''
        dict_repr = {}
        dict_repr['id'] = self._Base__id
        dict_repr['x'] = self._Rectangle__x
        dict_repr['size'] = self.size
        dict_repr['y'] = self._Rectangle__y
        return dict_repr
