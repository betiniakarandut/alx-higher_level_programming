#!/usr/bin/python3
# 0-read_file.py
# Betini Akarandut
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    file = with open(filename, 'r', encoding="utf-8")
    readfile = file.read()
    print(readfile, end="")
