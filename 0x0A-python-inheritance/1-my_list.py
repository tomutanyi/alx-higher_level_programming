#!/usr/bin/python3
"""Defines an inherited list class MyList is."""


class MyList(list):
    """Implements sorted printing for the built-in list classes."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
