#!/usr/bin/python3
""" A modult that contains a function to
divide all elements of a matrix (list of
lists) by div. div should not be zero. div
and matrix both are mandatory positional arguments
"""
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) not in [float, int]:
        raise TypeError('div must be a number')
    for li in matrix:
        if type(li) is not list:
            raise TypeError('matrix must be a matrix\
(list of lists) of integers/floats')
        for element in li:
            if type(element) not in [int, float]:
                raise TypeError('matrix must be a\
matrix (list of lists) of integers/floats')
    if len(matrix) > 0:
        row_length = len(matrix[0])
        for li in matrix:
            if len(li) != row_length:
                raise TypeError('Each row of the matrix must have the same size')
    new_matrix = []
    new_matrix_rows = 0
    for li in matrix:
        new_matrix.append([])
        new_matrix_rows += 1
        for element in li:
            new_matrix[new_matrix_rows - 1].append(round(element / div, 2))
    return new_matrix
