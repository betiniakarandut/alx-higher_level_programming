#!\usr\bin\python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
    except BaseException as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return False
    return True
