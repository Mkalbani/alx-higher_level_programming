#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """ cretaes student instances"""
    def __init__(self, first_name, last_name, age):
        """method to initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns directory description """
        return self.__dict__.copy()
