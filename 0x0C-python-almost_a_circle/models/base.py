#!/usr/bin/python3
"""
A module containing one class:
    "Base"
This class will be the baseclass for all the other classes in this
project. The goal of this is to avoid repeating the same code again
(by extension, same bugs)
"""
import json


class Base():
    """
    My baseclass
    """

    __nb_instances = 0

    def __init__(self, id=None):
        """
        Initializing method
        """
        self.id = id

    @property
    def id(self):
        """
        A property to retrieve "self.__id" to ensure "Encapsulation"
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        A setter to set "self.__id" to ensure "Encapsulation"
        """
        if value is not None:
            self.__id = value
        else:
            Base.__nb_instances += 1
            self.__id = Base.__nb_instances

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A method to return a JSON string of a list
        of dictionaries "list_dictionaries". If
        dict_dictionaries is empty the return value
        is "[]" (string type)
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return '"[]"'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A method to convert a list of objects
        into a string of the "json" format and
        write the result into "<Class_name>.json",
        where <Class_name> is the name of the class
        that is used to apply this method
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as my_file:
            list_dict = []
            if list_objs:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
            my_file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        A staticmethod to convert a JSON string
        representation into a python object.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        A method to create a new instance of "cls"
        using the keyword arguments in "dictionary"
        """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(2, 2, 2, 2)
            dummy_obj.update(**dictionary)
            return dummy_obj
        elif cls.__name__ == "Square":
            dummy_obj = cls(2)
            dummy_obj.update(**dictionary)
            return dummy_obj