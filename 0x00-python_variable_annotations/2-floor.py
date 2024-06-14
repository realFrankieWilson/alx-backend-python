#!/usr/bin/env python3
"""
Module `2-floor`
This module provides a type-annotated function that returns
the floor of a float.

Function:
  floor(n: float) -> int:
      Converts a float to an int and return the result.

      Arg:
          n (float): an argument of type float.

      Returns: The floor of the float `n`.
"""

import math


def floor(n: float) -> int:
    """
    Converts a float to an int and returns an integer value.

    Args:
        n (int): the float value.

    returns:
        An integer value.
    """
    return math.floor(n)
