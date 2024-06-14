#!/usr/bin/env python3
"""
Module `1-concat`
This module provides a function to concatinate two string.

Function:
  concat(str1: str, str2: str) -> str:
      Adds Concatinates two strings and return the result.

      Args:
          str1 (string): The first string.
          str2 (string): The second string.

      Returns: A concatinated string of `str1` and `str2`.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatinates two strings together and Returns a single string.

    Args:
        str1 (string): first string.
        str2 (string): second string.

    returns:
        concatinated string.
    """
    return str1 + str2
