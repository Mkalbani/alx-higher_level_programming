#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """returns the dictionary description of an obj"""

    i = {}
    if hasattr(obj, "__dict__"):
        i = obj.__dict__.copy()
    return i
