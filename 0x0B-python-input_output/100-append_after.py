#!/usr/bin/python3
"""
1st advanced task's solution
"""


def append_after(filename='', search_string='', new_string=''):
    """Modifying a text file
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        a_clone = lines[:]
        i = 0
        j = 0
        while i < len(lines):
            if search_string in lines[i]:
                a_clone.insert(i + 1, new_string)
                j += 1
            i += 1
            j += 1
        f.seek(0)
        f.writelines(a_clone)
