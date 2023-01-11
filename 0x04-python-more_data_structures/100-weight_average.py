#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    arc = 0
    ham = 0

    for din in my_list:
        arc += din[0] * din[1]
        ham += din[1]

    return (arc / ham)
