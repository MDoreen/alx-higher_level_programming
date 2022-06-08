#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary.keys())

    for i in keys:
        a_dictionary[i] *= 2

    return (a_dictionary)
