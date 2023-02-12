#!/usr/bin/python3
# Betini Akarandut
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
	"""Square module to inherit from Rectangle class."""

	def __init__(self, size, x=0, y=0, id=None):
		"""Initializes a new Square object.
		
		Args:
			size(int): the size of the new Square
			x(int): the x coordinate of the new Square
			y(int): the y coordinate of the new Square object
			id(int): the identity of new Square object 
		"""
		super().__init__(size, size, x, y, id)

	@property
	def size(self):
		"""Get/set the size of Square."""
		return self.width

	@size.setter
	def size(self, value):
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		"""Updates the Square object.

		Args:
			*args(int):
				1st argument rep the id attribute
				2nd argument rep the size attribute
				3rd argument rep the x coordinate attribute
				4th argument rep the y coordinate attribute
			**kwargs: Represents key/value pairs of attributes
		"""
		if args and len(args) != 0:
			a = 0
			for arg in args:
				if a == 0:
					if arg is None:
						self.__init__(self.size, self.x, self.y)
					else:
						self.id = arg
				elif a == 1:
					self.size = arg
				elif a == 2:
					self.x = arg
				elif a == 3:
					self.y = arg
				a += 1

		elif kwargs and len(kwargs) != 0:
			for k, v in kwargs.items():
				if k == "id":
					if v is None:
						self.__init__(self.size, self.x, self.y)
					else:
						self.id = v
					elif k == "size":
						self.size = v
					elif k == "x":
						self.x = v
					elif k == "y":
						self.y = v

	def to_dictionary(self):
		"""Returns the dictionary representation of the Square."""
		return {
			"id": self.id,
			"size": self.width,
			"x": self.x,
			"y": self.y
		}

	def __str__(self):
		"""returns printable Square object."""
		return "[Square] ({}) {}/{} - {}".format(
			                                      self.id,
			                                      self.x,
			                                      self.y,
			                                      self.width)
