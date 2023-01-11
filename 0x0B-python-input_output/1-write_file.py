#!/usr/bin/python3
"""contains functions that writes ro a text file"""


def write_file(filename="", text=""):
    """returns a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
