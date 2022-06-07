#!/usr/bin/python3
# File: 7-add_tuple.py
# Desc: A function that adds 2 tuples.

def add_tuple(tuple_a=(), tuple_b=()):
    size_a = len(tuple_a)
    size_b = len(tuple_b)

    if size_a == 0:
        a0 = 0
        a1 = 0
    elif size_a == 1:
        a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]

        if size_b == 0
        b0 = 0
        b1 = 0
    elif size_b == 1:
        b0 = tuple_b[0]
        b1 =0
    else:
        b0 = tuple_b[0]
        bi = tuple_b[1]

        new_tuple = (a0 + bo, a1 + b1)

        return (new_tuple)
