#!/usr/bin/env python3

"""
Module `2-measure_runtime`
Provides a function that measures the total execution time for `wait_n(n,, max_delay)`
and returns the average time per call
"""

import asyncio
import time
from typing import Callable

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for `wait_n(n, max_delay)` and
    returns the average time per call.

    Args:
        n (int): The number of `wait_random` coroutines to spawn.
        max_delay (int): The maximum delay in seconds for the `wait_random`
        coroutines.

    Returns:
        float: The average time per call of `wait_n(n, max_delay)`
        in seconds.
    """

    start_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_t = time.now()

    return (end_t - start_t) / n
