#!/usr/bin/python3
# Betini Akarandut
"""
Module to create a Rectangle class.
"""


class Rectangle:
	"""Defines a rectangle (based on 0-rectangle.py)."""
	
	def __init__(self, width=0, height=0):
		"""Initializes a class instance.
		
		Args:
			width(int): rectangle width
			height(int): rectangle height

		Return:
			None
		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""Get/set the width of the rectangle."""
		return(self.__width)

	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if (value < 0):
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""Get/set the height of the rectangle."""
		return(self.__height)

	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if (value < 0):
			raise ValueError("height must be >= 0")
		self.__height = value

	def area(self):
		"""Computes rectangle area."""
		return(self.__width * self.__height)

	def perimeter(self):
		"""Computes the perimeter of rectangle."""
		if (self.__width == 0 or self.__height == 0):
			return (0)

		return(2 * (self.__width + self.__height))

# my_rectangle = Rectangle(6, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# print("--")

# my_rectangle.width = 10
# my_rectangle.height = 3
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))