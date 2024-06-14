#!/usr/bin/env python3
"""
Module `9-element_length`
This module provides an annotated function parameter and return
values with the appropraite types

Function:
    to_kv takes string and OR float as arguments and returns
    a tuple.
        Args:
            k (string): A string of element.
            v (int | float): square of the value `v`
        returns:
            tuple

"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples, where each tuple conatins the origianl
    string and its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples,
        where each tuple contains the original string and its length.
    """
    return [(i, len(i)) for i in lst]
