#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) is not list:
        return
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
