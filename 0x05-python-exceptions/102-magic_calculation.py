#!/usr/bin/python3


def magic_calculation(a, b):
    """Does same thing as python bytecode provided."""

    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except ZeroDivisionError:
            result = a + b
            break
    return result
