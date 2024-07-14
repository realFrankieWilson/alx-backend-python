#!usr/bin/env python3

"""
`Module test_utils`
Provides a class `TestAccessNestedMap` that inherits from
unittest.TestCase.
"""

import unittest
from parameterized import parameterized  # type: ignore
from typing import Mapping, Sequence, Any
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A class that tests for a nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, map: Mapping[str, Any], path: Sequence[str], expected: Any
    ) -> None:
        """Test method that returns the expected output"""
        result = access_nested_map(map, path)
        self.assertEqual(result, expected)
