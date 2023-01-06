#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    dooku = len(sys.argv) - 1
    if dooku == 0:
        print("0 arguments.")
    elif dooku == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(dooku))
    for i in range(dooku):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
