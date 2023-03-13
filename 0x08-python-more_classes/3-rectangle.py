#!/usr/bin/python3

"""Define a rectangle"""

class Rectangle:

	"""Class Rectangle"""
	def__init__(self,width=0,height=0):
		self.width=width
		self.height=height
	@property
	def width(self):
		"""getter"""
		return self.__width=width
	@width.setter
	def width(self,value):
		"""setter"""
		if not isinstance(value,int):
			raise TypeError("width must be an integer")
		if value < 0 :
			raise ValueError("width must be >= 0")
		self.__width=value
	@property
	def height(self):
		"""getter"""
		return self.__height=height
	@height.setter
	def height(self,value):
		"""setter"""
		if not isinstance(value,int):
			raise TypeError("height must be an interger")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height=value
	def area(self):
		"""rectangle area"""
		return (self.__height * self.__width)
	def perimeter(self):
		"""rectangle perimeter"""
		if self.__width==0 or self.__height==0:
			return (0)
	def __str__(self):
		if self.__width == 0 or self.__height == 0:
			return ("")
		rect = []
		for i in range(self.__height):
			[rect.append('#') for j in range(self.__width)]
			if i != self.__height - 1:
			rect.append("\n")
		return ("".join(rect))


	

