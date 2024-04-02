#!/usr/bin/python3
""" A modult containing one function
"matrix_divided". It's the solution
of the second task of the project
"0x07-python-test_driven_development"
"""


def matrix_divided(matrix, div):
    """ A function to return a mtrix of each
    element is the result of the corresponding
    element in the original matrix divided by
    (div).matrix should be a list of lists of
    integer or floats, otherwise errors will occur.
    div must not be 0, otherwise an error will occur.
    If matrix is empty, the result is an empty
    matrix.
    """

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
                raise TypeError('Each row of the \
matrix must have the same size')
    new_matrix = []
    new_matrix_rows = 0
    for li in matrix:
        new_matrix.append([])
        new_matrix_rows += 1
        for element in li:
            new_matrix[new_matrix_rows - 1].append(round(element / div, 2))
    return new_matrix
