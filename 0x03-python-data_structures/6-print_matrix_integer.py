#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) is not list:
        return
    for i in matrix:
        if type(i) is not list:
            return
    if not (len(matrix)):
        print()
        return
    for my_list in matrix:
        for element in range(len(my_list)):
            if (element == (len(my_list) - 1)):
                print("{:d}".format(my_list[element]))
            else:
                print("{:d} ".format(my_list[element]), end="")
