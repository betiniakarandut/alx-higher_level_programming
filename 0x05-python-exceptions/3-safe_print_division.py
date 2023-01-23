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
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    print("")
    return (div)
