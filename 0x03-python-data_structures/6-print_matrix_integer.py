#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not (len(matrix)):
        print()
    for my_list in matrix:
        for element in range(len(my_list)):
            if (element == (len(my_list) - 1)):
                print("{:d}".format(my_list[element]))
            else:
                print("{:d} ".format(my_list[element]), end="")
