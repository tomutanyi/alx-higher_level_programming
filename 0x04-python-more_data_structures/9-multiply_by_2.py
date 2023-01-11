#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    quor_dict = {x: (a_dictionary[x] * 2) for x in a_dictionary}

    return quor_dict
