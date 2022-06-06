#!/usr/bin/python3
# 0-print_list_interger.py
# Desc: Function that prints all intergers of a list

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
