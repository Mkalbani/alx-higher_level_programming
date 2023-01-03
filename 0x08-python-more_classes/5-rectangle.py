#!/usr/bin/python3
"""
Defines A Class Rectangle
"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes The Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for Private Instant Attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for Private Instant Attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for Private Instant Attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """"height setter, private instance attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """define Area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """"defines perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Printable representataion of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return("".join(rect))

    def __repr__(self):
        """string representation of rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of
        the rectangle.
        """
        print("Bye rectangle...")
