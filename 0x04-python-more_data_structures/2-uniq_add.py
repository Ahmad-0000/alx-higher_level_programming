#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return reduce(lambda x, y: x + y, new_list)
