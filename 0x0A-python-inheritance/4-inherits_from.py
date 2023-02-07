#!/usr/bin/python3
# 4-inherits_from.py
# Betini Akarandut
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is an inherited instance of a_class.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
