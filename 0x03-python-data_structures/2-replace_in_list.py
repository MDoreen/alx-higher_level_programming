#!/usr/bin/python3
# File: 2-replace_in_list.py
# Desc: A function that replaces an element of a
# list at a specific position (like in C)

def replace_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) < idx:
        return (my_list)

    my_list[idx] = element
    return (my_list)
