#!/usr/bin/python3
# File: 6-print_matrix_integer.py
# Desc: function that prints a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            if m != 0:
                print(" ", end='')
            print("{:d}".format(matrix[n][m]), end='')
        print()
