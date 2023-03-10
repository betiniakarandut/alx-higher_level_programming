#!/usr/bin/python3
# 0-safe_print_list.py
# Author:Betini Akarandut


def safe_print_list(my_list=[], x=0):
    """Prints element of a list.

    Args:
        my_list(List): List to print out element from.
        x(int): Number of items to print from the list.

    Returns:
        The number of items printed.

    """

    try:
        for y in range(x):
            print("{}".format(my_list[y]), end="")
    except IndexError:
        print()
        return y
    print()
    return x
