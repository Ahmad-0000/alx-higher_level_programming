#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if not (length):
        return None
    i = my_list[0]
    for current in my_list:
        if (current > i):
            i = current
    return i
