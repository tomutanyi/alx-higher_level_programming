#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    expo = []
    for i in range(len(my_list)):

        if my_list[i] % 2 == 0:
            expo.append(True)
        else:
            expo.append(False)

    return (expo)
