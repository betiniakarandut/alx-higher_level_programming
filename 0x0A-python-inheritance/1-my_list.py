#!/usr/bin/python3
# 1-my_list.py
# Betini Akarandut
"""Defines an inherited list class MyList."""


class MyList(list):
    """Uses sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
