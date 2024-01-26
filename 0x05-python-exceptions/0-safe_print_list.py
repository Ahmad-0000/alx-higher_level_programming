#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for element in my_list:
        if i >= x:
            break
        try:
            print(f'{my_list[i]}', end="")
        except IndexError:
            pass
        i += 1
    print()
    return i
