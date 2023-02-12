#!/usr/bin/python3
# Betini Akarandut
"""Base class for other classes."""
import json
import csv
import turtle


class Base:
	"""Defines Base class.
	This is the parent class of all other classes.

	Attributes:
	__nb_objects(int): Private class instance attribute
	"""

	__nb_objects = 0

	def __init__(self, id=None):
		"""Initialize new object of Base class.

		Args:
			id (int): id of the new instance Base class
		"""

		if id is not None:
		self.id = id
		else:
		Base.__nb_objects += 1
		self.id = Base.__nb_objects