#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a(int): First integer.
        b(int): Second integer.

    Returns:
        The division of a by b.
    """
    try:
        result = a / b
    except ArithmeticError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result