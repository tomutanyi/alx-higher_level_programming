#!/usr/bin/python3
""" A locked class """

class LockedClass():
    """No attribute creations unless attribute = firs_name"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init methods"""
        pass
