#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    _1st_t_len = len(tuple_a)
    a1, b1, a2, b2 = 0, 0, 0, 0
    if (_1st_t_len == 1):
        a1 = tuple_a[0]
    elif (_1st_t_len == 0):
        pass
    else:
        a1, b1 = tuple_a[0], tuple_a[1]
    _2nd_t_len = len(tuple_b)
    if (_2nd_t_len == 1):
        a2 = tuple_b[0]
    elif (_2nd_t_len == 0):
        pass
    else:
        a2, b2 = tuple_b[0], tuple_b[1]
    return (a1 + a2, b1 + b2)
