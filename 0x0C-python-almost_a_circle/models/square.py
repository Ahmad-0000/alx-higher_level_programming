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
        return f'[Square] ({self.id}) {self._Rectangle__x}/\
{self._Rectangle__y} - {self._Rectangle__width}'

    @property
    def size(self):
        '''
        A property to retrive "size" attribute
        '''
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        '''
        A setter to set "size" attribute
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        '''
        A method to update id, size, x and y. if "args"
        is present and not empty, it will be used, otherwise
        "kwargs" will be used for updating
        '''
        if args:
            my_list = []
            for arg in args:
                l.append(arg)
            my_list = tuple(l)
            if len(my_list) == 1:
                self.id = args[0]
            elif len(my_list) == 2:
                self.id, self.size = args
            elif len(my_list) == 3:
                self.id, self.size, self.x = args
            elif len(my_list) == 4:
                self.id, self.size, self.x, self.y = args
        elif kwargs:
            keys = kwargs.keys()
            for key in keys:
                if key == "id":
                    self.id = kwargs[f'{key}']
                if key == "size":
                    self.size = kwargs[f'{key}']
                if key == "x":
                    self.x = kwargs[f'{key}']
                if key == "y":
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
