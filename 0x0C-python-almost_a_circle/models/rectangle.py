#!/usr/bin/python3
"""Defines a class Rectangle that inherits from the class Base"""
Base = __import__("base").Base


class Rectangle(Base):
    """This defines a class Rectangle that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates Rectangle instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the the value of the width attribute"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.__width = width

    @property
    def height(self):
        """Retrieves the height attribute value"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the value of the height attribute"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__height = height

    @property
    def x(self):
        """Retrieves the x attribute value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x attribute value"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        self.__x = x

    @property
    def y(self):
        """Retrieves the y attribute value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y attribute value"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        self.__y = y

    def area(self):
        """Public method that returns the area of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """Public method that prints in stdout the Rectangle instance with the character #"""
        rect = []
        for i in range(self.height):
            [rect.append("#") for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        print("".join(rect))
