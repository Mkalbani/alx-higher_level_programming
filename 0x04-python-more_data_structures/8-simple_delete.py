#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i, value in list(a_dictionary.items()):
        if i == key:
            del a_dictionary[key]
    return 
