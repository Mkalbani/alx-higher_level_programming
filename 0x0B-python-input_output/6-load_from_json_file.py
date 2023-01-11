#!/usr/bin/python3
"""functions creates an obj from a json file"""

import json


def load_from_json_file(filename):
    """creates obj from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
