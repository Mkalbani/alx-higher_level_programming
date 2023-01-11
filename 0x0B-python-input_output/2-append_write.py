#!/usr/bin/python3
""" function appends string at the end"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
