#!/usr/bin/python3
'''
A module containing one class:
    "Base"
This class will be the baseclass for all the other classes in this
project. The goal of this is to avoid repeating the same code again
(by extension, same bugs)
'''
import json
import os


class Base():
    '''
    My baseclass, this is the class from which
    all other classes will inherit, thus, they
    will access to its attributes and methods
    including the __init__() method
    '''

    __nb_instances = 0

    def __init__(self, id=None):
        '''
        Initializing method to intialize an instance
        with an optional id.
        '''
        self.id = id

    @property
    def id(self):
        '''
        A property to retrive "self.__id" to ensure "Encapsulation"
        principle, thus, the person can access the private attribute
        "__id" without messing with the class implementation
        '''
        return self.__id

    @id.setter
    def id(self, value):
        if value is not None:
            self.__id = value
        else:
            Base.__nb_instances += 1
            self.__id = Base.__nb_instances

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        A method to return a JSON string of a list
        of dictionaries "list_dictionaries". If
        dict_dictionaries is empty the return value
        is "[]" (string type)
        '''
        if not list_dictionaries or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        A method to convert a list of objects
        into a string of the "json" format and
        write the result into "<Class_name>.json",
        where <Class_name> is the name of the class
        that is used to apply this method
        '''
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as my_file:
            dict_list = []
            if list_objs:
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
            my_file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        '''
        A staticmethod to convert a JSON string
        representation into a python object.
        '''
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        A method to create a new instance of "cls"
        using the keyword arguments in "dictionary"
        '''
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy_obj = cls(2)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        '''
        A class method that loads a JSON list contining
        objects (dictionary representations) from a .json
        file, and returns a list of real created objects
        '''
        filename = f"{cls.__name__}.json"
        if os.path.isfile(filename):
            return_value = []
            with open(filename, encoding="utf-8") as my_file:
                file_list = cls.from_json_string(my_file.read())
                for dictionary in file_list:
                    return_value.append(cls.create(**dictionary))
                return return_value
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, objs_list):
        """Saving objects representations in a csv file
        """
        filename = f'{cls.__name__}.csv'
        lines = []
        if cls.__name__ == "Rectangle":
            for obj in objs_list:
                lines.append(f"{obj.id},{obj.width},{obj.height},"
                             f"{obj.x},{obj.y}\n")
        elif cls.__name__ == "Square":
            for obj in objs_list:
                lines.append(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")
        with open(filename, "w", encoding="utf-8") as csvfile:
            csvfile.writelines(lines)

    @classmethod
    def load_from_file_csv(cls):
        """Loading objects from a csv file
        """
        filename = cls.__name__ + ".csv"
        objs = []
        with open(filename, "r", encoding='utf-8') as csvfile:
            lines = csvfile.readlines()
            for line in lines:
                fields = line.split(',')
                if len(fields) == 4:
                    field1, field2, field3, field4 = fields
                    attributes = {k: v for k, v in [
                                                    ("id", int(field1)),
                                                    ("size", int(field2)),
                                                    ("x", int(field3)),
                                                    ("y", int(field4))
                                                    ]
                                }
                    objs.append(cls.create(**attributes))
                elif len(fields) == 5:
                    field1, field2, field3, field4, field5 = fields
                    attributes = {k: v for k, v in [
                                                    ("id", int(field1)),
                                                    ("width", int(field2)),
                                                    ("height", int(field3)),
                                                    ("x", int(field4)),
                                                    ("y", int(field5))
                                                   ]
                                 }
                    objs.append(cls.create(**attributes))
        return objs
