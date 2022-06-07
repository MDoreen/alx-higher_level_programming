#!/usr/bin/python3
# File: 5-no_c.py
# Desc: A function that removes all characters c and C from a string.

def no_c(my_string):
    length = len(my_string)

    n = 0

    new_string = my_string[:]

    for i in range(length):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_string = new_string[:(i - n)] + my_string[(i + 1):]
            n += 1

    return (new_string)
