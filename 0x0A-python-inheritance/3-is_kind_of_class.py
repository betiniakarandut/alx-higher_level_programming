#!/usr/bin/python3
# 3-is_kind_of_class.py
# Betini Akarandut
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to check.
    Returns:
        True - If obj is an instance or inherited instance of a_class.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
