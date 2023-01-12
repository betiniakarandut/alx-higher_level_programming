#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(j, a_dictionary[j])) for j in sorted(a_dictionary)]
