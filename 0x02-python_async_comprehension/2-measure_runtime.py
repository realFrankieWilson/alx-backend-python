#!/usr/bin/env python3

"""
Module `2-measures`
Imports a coroutine `async_comprehension`, executes the imported function
four times and measure the total runtime.
"""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that execute and measure the total runtime of
    another coroutine function.
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = time.time()
    return end_time - start_time
