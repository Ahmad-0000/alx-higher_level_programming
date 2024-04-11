#!/usr/bin/python3

def remove_char_at(string, n):
    if ((type(string) is not str) or (type(n) is not int)):
        return
    i = 0
    new_string = ''
    for j in string:
        if i == n:
            pass
        else:
            new_string += j
        i += 1
    return new_string
