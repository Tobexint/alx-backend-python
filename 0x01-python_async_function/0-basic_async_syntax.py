#!/usr/bin/env python3
"""
This module contains a coroutine, async_generator, with no arguments looping
 10 times, each time asynchronously wait 1 second, then yield a random number
 between 0 and 10. random module is used.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async coroutine that takes an integer argument
    Args:
        max_delay(int) delay coroutine
    Return:
        random value(float)
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
