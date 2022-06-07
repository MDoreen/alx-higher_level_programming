#!/usr/bin/python3
# File: 5-no_c.py
# Desc: function that removes all characters c and C from a string.

def no_c(my_string):
    new_string = my_string[:]
    i = 0

    for n in range(len(new_string)):
        if my_string[n] == 'c' or my_string[n] == 'C':
            new_string = new_string[:(n - i)] + my_string[(n + 1):]
            i += 1

    return (new_string)i
