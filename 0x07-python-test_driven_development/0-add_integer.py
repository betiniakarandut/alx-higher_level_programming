#!/usr/bin/python3
# file_name: 0-add_integer.py
# Betini Akarandut <betiniakarandut@gmail.com>

"""
Module to compute sum of two integers
"""


def add_integer(a, b=98):
	"""Sums two integers
	
	Args:
		a(int) - first integer variable
		b(int) - second integer variable

	Returns:
		sum of a and b
	"""

	if ((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, int))):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))