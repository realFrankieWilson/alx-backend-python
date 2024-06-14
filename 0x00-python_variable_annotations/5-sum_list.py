#!/usr/bin/env python3
"""
Module `5-sum_list`
This module provides a function to sum the elements of a list.

Function:
  sum_list(input_list: list) -> float:
      Adds the item of a list and return the result.

      Args:
          input_list (float): list of floats.

      Returns: The sum of list as a `float`.
"""

from typing import List, Union


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all elements in the input list
    and returns the result as a float.

    Args:
        input_list (List[float]): The list of floating-point
        numbers to be summed.

    returns:
        float: The sum of all elements in the input_list.
    """
    return sum(input_list)
