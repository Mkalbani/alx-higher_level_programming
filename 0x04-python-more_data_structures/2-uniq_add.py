#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    for j in set(my_list):
        i += j
    return i
