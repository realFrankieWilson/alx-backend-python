#!/usr/bin/env python3
"""
Module `7-to_kv`
This module provides a function that takes a string k and
int ORfloat v as arguments
and returns a tuple.

Function:
    to_kv takes string and OR float as arguments and returns
    a tuple.
        Args:
            k (string): A string of element.
            v (int | float): square of the value `v`
        returns:
            tuple

"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Calculates the sum of all elements in the input list
    and returns the result as a float.

    Args:
        mxd_lst Union([List[float], List[int]): The list of
        mxd elements

    returns:
        float: The sum of all elements in the mxd_list.
    """
    return (k, v**2)
