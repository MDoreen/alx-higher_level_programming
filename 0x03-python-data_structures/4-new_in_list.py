#!/usr/bin/python3
# File: 4-new_in_list.py
# Desc: A function that replaces an element in a list at
# a specific position without modifying the original list (like in C)

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    new_list = my_list[:]
    new_list[idx] = element

    return (new_list)