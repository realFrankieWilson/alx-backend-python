#!/usr/bin/env python3

"""
Module `0-async_generator`
Provides a coroutine `async_generator` that yield a random number between
0 and 10.
"""

import random
import asyncio


async def async_generator() -> None:  # type: ignore
    """
    Loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)