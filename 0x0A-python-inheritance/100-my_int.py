#!/usr/bin/python3
"""Defines a class MyInt that inheriits from int."""


class MyInt(int):
    """Invert int operaators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
