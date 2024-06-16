#!/usr/bin/env python3

"""
Module `1-concurrent_coroutines`
An async routine called `wait_n` that spans `wait_random` coroutines and
returns the list of delays in ascending order.
"""

import asyncio
from typing import List

wait_r = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` instances of the `wait_random` coroutine with the specified
    `max_delay`,
    and returns the list of delays in ascending order.

    Args:
        n (int): The number of `wait_random` coroutines to spawn.
        max_delay (int): The maximum delay in seconds for the `wait_random1
        coroutins.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = await asyncio.gather(*[wait_r(max_delay) for _ in range(n)])
    return sorted(delays)
