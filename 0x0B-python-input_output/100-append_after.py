#!/usr/bin/python3
"""
1st advanced task's solution
"""


def append_after(filename='', search_string='', new_string=''):
    """Modifying a text file
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.writelines(lines)
