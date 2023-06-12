#!/usr/bin/python3
"""Defines a Rectangle subclass Squareee."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a squaree."""

    def __init__(self, size):
        """Initialize a new squaree.
        Args:
            size (int): The size of the new squaree.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
