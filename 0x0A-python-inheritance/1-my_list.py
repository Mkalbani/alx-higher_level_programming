#!/usr/bin/python3
"""The Class MyList"""


class MyList(list):
    """Sub Class That Prints Sorted list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints soreted list"""
        print(sorted(self))
