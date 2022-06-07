#!/usr/bin/python3
# File: 3-print_reversed_list_integer.py
# Desc: A function that prints all integers of a list, in reverse order.

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
