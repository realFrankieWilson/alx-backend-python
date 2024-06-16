#!/usr/bin/env python3

"""
Module `0-basic_async_syntax`
An Asynchronous coroutin that profide an interger argument named `wait_random`
that waits for a random delay between 0 and `max_delay`
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds
    and returns the delay

    Args:
        max_delay (int, optional): The maximun delay in seconds
        Defaults to 10.
    Returns:
        float: The actual delay in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return float(delay)
