#!/usr/bin/python3
# 102-complex_delete.py


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for i, v in a_dictionary.items():
            if v == value:
                del a_dictionary[i]
                break

    return (a_dictionary)