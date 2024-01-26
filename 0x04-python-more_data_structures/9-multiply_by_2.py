#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict()
    for i in a_dictionary.keys():
        new_dictionary[str(i)] = a_dictionary[str(i)] * 2
    return new_dictionary
