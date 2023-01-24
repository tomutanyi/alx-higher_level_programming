#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the result of a divideed by b."""

    try:
        loc = a / b

    except (TypeError, ZeroDivisionError):
        loc = None

    finally:
        print("Inside result: {}".format(loc))
    return (loc)
