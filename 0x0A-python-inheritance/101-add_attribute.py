#!/usr/bin/python3
"""
This module sets an attribute in an object
"""


def add_attribute(obj, name, value):
    """
    This method checks if an attribute exists and sets it to value

    Args:
        obj: object to check
        name: name of the attribute
        value: value to set the attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
