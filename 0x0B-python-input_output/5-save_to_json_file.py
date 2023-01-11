#!/usr/bin/python3
""" Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """writes obj to textfile using json"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
