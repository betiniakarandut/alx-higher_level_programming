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
    res = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            res += 1
        except (IndexError, IndentationError):
            print("Oops! Please give proper index")
            break
    print("")
    return (res)
