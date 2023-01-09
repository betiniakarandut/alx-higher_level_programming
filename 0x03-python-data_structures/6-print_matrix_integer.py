#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            print("{:d}".format(matrix[a][b]), end="")
            if b != (len(matrix[a]) - 1):
                print(" ", end="")

        print("")
