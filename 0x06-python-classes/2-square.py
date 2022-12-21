#!/usr/bin/python3
"""Square Class Defination"""


class Square:
    """Private instance attri
    bute
    """
    def __init__(self, size=0):
        """initializes an optional
        size

        Args:
            __size (int): The __size 
            the new square.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
