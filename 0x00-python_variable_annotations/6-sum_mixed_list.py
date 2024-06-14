#!/usr/bin/env python3
"""
Module `6-sum_mixed_list`
This module provides a function to sum the elements of a mixed complex list.

Function:
  sum_mixed_list(mxd_lst: list) -> float:
      Adds the item of a mixed list and return the result.

      Args:
          mxd_lst (float): list of mixed type.

      Returns: The sum of list as a `float`.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of all elements in the input list
    and returns the result as a float.

    Args:
        mxd_lst Union([List[float], List[int]): The list of
        mxd elements

    returns:
        float: The sum of all elements in the mxd_list.
    """
    return sum(mxd_lst)
