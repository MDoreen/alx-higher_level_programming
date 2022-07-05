#!/usr/bin/python3
"""
This module creates an BaseGeometry class
"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value argument

        Args:
            name (String): string
            value (int): value to validate
        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
