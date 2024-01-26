#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_a_len = len(tuple_a)
    a1, b1, a2, b2 = 0, 0, 0, 0
    if (t_a_len == 1):
        a1 = tuple_a[0]
    elif (t_a_len == 0):
        pass
    else:
        a1, b1 = tuple_a
    t_b_len = len(tuple_b)
    if (t_b_len == 1):
        a2 = tuple_b[0]
    elif (t_b_len == 0):
        pass
    else:
        a2, b2 = tuple_b
    return (a1 + a2, b1 + b2)
