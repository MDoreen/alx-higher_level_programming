#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    fin_matrix = matrix.copy()

    for n in range(len(matrix)):
        fin_matrix[n] = list(map(_square, matrix[n]))

    return (fin_matrix)


def _square(num):
    return (num ** 2)
