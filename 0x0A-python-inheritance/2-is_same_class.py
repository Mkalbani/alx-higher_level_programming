#!/usr/bin/python3
"""This Module contains the function is_same_class"""


def is_same_class(obj, a_class):
    """returns true if object s exactly an instance of the specified class """
    return (type(obj) == a_class)
