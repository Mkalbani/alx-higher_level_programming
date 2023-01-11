#!/usr/bin/python3
""" contains JSON representation of an obj
import module"""
import json


def to_json_string(my_obj):
    """returns  the JSON representation of an object"""
    return json.dumps(my_obj)
