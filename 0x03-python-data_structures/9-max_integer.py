#!/usr/bin/python
# File: 9-max_integer.py
# Desc: A function that finds the biggest integer of a list

def max_integer(my_list=[]):
   if len(my_list) == 0 or not my_list:
        return (None)

    return sorted(my_list)[-1]
