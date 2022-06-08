#!/usr/bin/python3
# File: 1-search_replace.py
# Desc: A function that replaces all occurrences of an element
# by another in a new list

def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for i in range(0, (len(my_list))):
        if my_list[i] == search:
            new_list[i] = replace

    return (new_list)
