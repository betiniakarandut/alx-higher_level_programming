#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    biggest_num = my_list[0]
    for a in range(len(my_list)):
        if my_list[a] > biggest_num:
            biggest_num = my_list[a]

    return (biggest_num)

