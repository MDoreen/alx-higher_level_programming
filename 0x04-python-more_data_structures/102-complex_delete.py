#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()

    for key, val in new_dict.items():
        if value == val:
            new_dict.pop(key)

    return new_dict
