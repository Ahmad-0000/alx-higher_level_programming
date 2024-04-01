#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    line_beginning = 1
    for char in text:
        if ord(char) == ord(' ') and line_beginning == 1:
            pass
        elif ord(char) == ord('.') or ord(char) == ord('?') or ord(char) == ord(':'):
            line_beginning = 1
            print(char + '\n\n', end="")
        elif ord(char) != ord(' ') and line_beginning == 1:
            print(char, end="")
            line_beginning = 0
        else:
            print(char, end="")
