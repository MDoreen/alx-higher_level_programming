#!/usr/bin/python3
# file: 1-element_at.py
# Desc: A function that retrieves an element from a list like in C

def element_at(my_list, idx):
    if idx < 0:
        return (None)

    lenght = len(my_list)

    if idx > lenght - 1:
        return (None)

    return(my_list[idx])
