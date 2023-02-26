#!/usr/bin/python3

"""Setters and getters"""

class Square:

	def __init__(self,size):
		self.size=size

	def size(self):
		self._size=size

		if not isinstance(size,int):
			raise TypeError("size must be an interger")
		elif size <0:
			raise ValueError("size must be >=0")
	
		self._size=value

	def area(self):
		return(self._size*self._size)
