#!/usr/bin/env python3

"""
Module `1-async_comprehension`
Imports a coroutine `async_generator`, collects 10 random numbers
using an async comprehension over async_generator, then return
the 10 random numbers.
"""

import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [obj async for obj in async_generator()]
