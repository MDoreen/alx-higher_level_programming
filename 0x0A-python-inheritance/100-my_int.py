#!/usr/bin/python3
"""
This module creates a class that inherits from int
"""


class MyInt(int):
    """This is an inverted class"""
    def __eq__(self, other):
        """returns not equal to"""
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """returns equal to"""
        return (int.__eq__(self, other))
