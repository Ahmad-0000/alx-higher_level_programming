#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ""
    for i in range(len(my_string) - 1):
        if (my_string[i] == 'c') or (my_string[i] == 'C'):
            my_new_string = my_new_string
        else:
            my_new_string = my_new_string + my_string[i]
    return my_new_string
