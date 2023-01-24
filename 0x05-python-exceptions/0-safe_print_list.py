#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    lini = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            lini += 1
        except IndexError:
            break
    print("")
    return (lini)
