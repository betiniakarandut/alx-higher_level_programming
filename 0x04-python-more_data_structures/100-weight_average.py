#!/usr/bin/python3
# 100-weight_average.py


def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not forinstance(my_list, list) or len(my_list) == 0:
        return (0)

    mean = 0
    size = 0
    for list_tuple in my_list:
        mean += (list_tuple[0] * list_tuple[1])
        size += list_tuple[1]
    return (mean / size)
