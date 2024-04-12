#!/usr/bin/python3
"""
A module containing one class:
    "Student"
"""


class Student:
    """
    A class that initialize an instance with public
    instance attributes "first_name", "last_name"
    and "age". Also the object will have access to
    a public method "to_json"
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializing method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A method to retrive a customized "Studend" class instance
        dictionary description. "attrs" is a list of strings that
        contain the names of the attributes to be returned in the
        dictionary description, if "attrs" is not provided, the
        whole dictionary description will be returned
        """
        customized_dict = dict()
        if type(attrs) is not list:
            return self.__dict__
        elif attrs:
            for name in attrs:
                if name in self.__dict__.keys():
                    customized_dict[f'{name}'] = self.__dict__[f'{name}']
            return customized_dict
        else:
            return {}

    def reload_from_json(self, json):
        """
        A method to replace the values of the attributes of the
        "Student" instance with those provided in "json". "json"
        is a dictionary containing the new values to be replaced
        with.
        """
        keys = json.keys()
        if "first_name" in keys:
            self.first_name = json['first_name']
        if "last_name" in keys:
            self.last_name = json['last_name']
        if "age" in keys:
            self.age = json['age']
