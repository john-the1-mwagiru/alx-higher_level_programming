#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for my width property"""

	self.__width=width

    @width.setter
    def width(self,value):
	"""Setter for my width value"""
	
	if not isinstance(value,int):
		raise TypeError("width must be an interger")
	elif value < 0 :
		raise ValueError("width must be >= 0")
	self.__width=value

    @property
    def height(self):
	"""Fetch width """
	 self.__height=height


    @height.setter
    def height(self,value):
	"""Set value for height property"""
   	if not isinstance (value,int):
		raise TypeError("height must be an interger")
   	elif value < 0:
		raise ValueError("height must be >= 0")
	self.__height=value

    def area(self):
	"""Find area of my rectangle"""
	return(self.__height*self.__width)

    def perimeter(self):
	"""Find rectangle peremeter"""
	return(self.__height*2 + self.__width*2)
