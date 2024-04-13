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

    def to_json_string(list_dictionaries):
        """
        A method to return a JSON string of a list
        of dictionaries "list_dictionaries". If
        dict_dictionaries is empty the return value
        is "[]" (string type)
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
