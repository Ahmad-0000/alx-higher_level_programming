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
        super().__init__(size, size, x, y)

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
            i = 0
            private_attrs = ['__id', '__size', '__x', '__y']
            for j in args:
                if i == 4:
                    break
                elif i == 0:
                    self._Base__id = j
                elif i == 1:
                    self.size = j
                else:
                    self.__dict__[f'_Rectangle{private_attrs[i]}'] = j
                i += 1
        else:
            if kwargs:
                keys = kwargs.keys()
                for key in keys:
                    if key == 'id':
                        self._Base__id = kwargs[key]
                    elif key == 'size':
                        self.size = kwargs[key]
                    else:
                        self.__dict__[f'_Rectangle__{key}'] = kwargs[key]

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
