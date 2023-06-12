#!/usr/bin/python3
"""Defines an object attribute lookup function to use."""


def lookup(obj):
    """Return a list of an object's available attributes to use."""
    return (dir(obj))
