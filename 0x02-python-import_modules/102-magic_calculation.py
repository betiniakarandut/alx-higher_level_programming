#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b):
    """Match bytecode provided by ALX-Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        j = add(a, b)
        for i in range(4, 6):
            j = add(j, i)
        return (j)

    else:
        return(sub(a, b))
