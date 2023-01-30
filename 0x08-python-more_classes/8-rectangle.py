#!/usr/bin/python3
# Betini Akarandut
"""
Module to create a Rectangle class.
"""


class Rectangle:
	"""Defines a rectangle (based on 0-rectangle.py)."""
	
	number_of_instances = 0
	print_symbol = "#"

	def __init__(self, width=0, height=0):
		"""Initializes a class instance.
		
		Args:
			width(int): rectangle width
			height(int): rectangle height

		Return:
			None
		"""
		type(self).number_of_instances += 1
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

	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		"""Returns the biggest rectangle based on the area.

		Args:
			rect_1(Rectangle): The first Rectangle instance.
			rect_2(Rectangle): The second Rectangle instance.

		Raises:
			TypeError: If either cases of rect_1 and rect_2 is false.
		"""

		if not isinstance(rect_1, Rectangle):
			raise TypeError("rect_1 must be an instance of Rectangle")
		if not isinstance(rect_2, Rectangle):
			raise TypeError("rect_2 must be an instance of Rectangle")
		if rect_1.area() >= rect_2.area():
			return (rect_1)
		return (rect_2)

	def __str__(self):
		"""Return printable representation of the Rectangle.

		Represents the rectangle with the # character.
		"""

		if self.__width == 0 or self.__height == 0:
		    return ("")

		draw_rect = []
		for i in range(self.__height):
		    [draw_rect.append(str(self.print_symbol)) for j in range(self.__width)]
		    if i != self.__height - 1:
		        draw_rect.append("\n")
		return ("".join(draw_rect))

	def __repr__(self):
		"""Return string representation of the Rectangle."""
		draw_rect = "Rectangle(" + str(self.__width)
		draw_rect += ", " + str(self.__height) + ")"
		return (draw_rect)

	def __del__(self):
		"""Prints a message each instance a rectangle is deleted."""

		type(self).number_of_instances -= 1
		print("Bye rectangle...")