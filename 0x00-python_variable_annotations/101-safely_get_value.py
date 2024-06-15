#!/usr/bin/env python3

"""
Module `101-safely_get_value`
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union [T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given key from the dictionary.
    If the key is not found in the dictionary, the default value is returned.

    Args:
        dct (Dict[Any, T]): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (T): The default value to return if the key is not found.

    Returns:
        T: The value associated with the given key, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default