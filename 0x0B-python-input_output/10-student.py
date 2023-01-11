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
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                return obj
            d_list = {}
            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list
        return obj
