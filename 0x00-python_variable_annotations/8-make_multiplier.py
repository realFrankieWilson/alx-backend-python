#!/usr/bin/env python3
"""
Module `8-make_multiplier`
This module provides a function that takes a float multiplier as
as argument and returns a function that muliplies
a float by multiplier.

Function:
    to_kv takes string and OR float as arguments and returns
    a tuple.
        Args:
            k (string): A string of element.
            v (int | float): square of the value `v`
        returns:
            tuple

"""

from typing import Callable, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a new function that multiplies a float by the given factor.

    Args:
        multplier (float): The number to multiply by

    returns:
        Callable[[float], float]: A new function that takes a float
        and returns the result of multiplying it by the factor.
    """

    def multiply(x: float) -> float:
        """
        Multiplies the input float by the multplier.

        Args:
            x (float): The number to be multiplied

        Returns:
            float: The result of multiplying mul by multiplier.
        """
        return x * multiplier

    return multiply
