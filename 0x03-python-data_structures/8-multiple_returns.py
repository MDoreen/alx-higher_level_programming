#!/usr/bin/python3
# File: 8-multiple_returns.py
# Desc: A function that returns a tuple with the length of a string
# and its first character

def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        first = None
    else:
        first = sentence[0]

    new_tuple = (length, first)
    return (new_tuple)
