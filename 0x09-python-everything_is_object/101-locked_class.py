#!/usr/bin/python3
"""
This contains a class that prevents the user from dynamically
creating new instance attributes
"""


class LockedClass:
    """
    This class preventst the user from dynamically
    creating new instance attributes,
    except if the new instance attribute is called first_name
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """initialized an object of a class"""
        pass
