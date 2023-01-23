#!/usr/bin/python3


def magic_calculation(a, b):
    """Returns the result of op a and b."""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except (ValueError, TypeError):
            result = b + a
            break
    return (result)
