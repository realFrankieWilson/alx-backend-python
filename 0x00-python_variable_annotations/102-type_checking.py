#!/usr/bin/env python3

"""
Module `102-type_checking`
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    This function is validated using mypy after some necessary
    modification has been made.
    """
    zoomed_in: tuple[int] = tuple(item for item in lst for _ in range(factor))
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
