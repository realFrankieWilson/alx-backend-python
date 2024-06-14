#!/usr/bin/env python3
"""
Module `100-safe_first_element`
This module provides an annotated function parameter and return
values with the appropraite types
"""

from types import NoneType
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Returns the first element of the input list if it's not empy,
    Otherwise returns None.

    Args:
        lst (Any): An iterable of any type.

    Returns:
        Optional[Any]: The first element of the input list if it's not
        empy, otherwise Noen is returned.
    """
    if lst:
        return lst[0]
    else:
        return None
