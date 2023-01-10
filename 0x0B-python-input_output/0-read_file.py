#!/usr/bin/python3
""" Contains a function that reads a text file"""


def read_file(filename=""):
    """returns txtfile in stdout"""
    with open(filename, encoding="utf-8") as f:
        readText = f.read()
        print(readText, end='')
