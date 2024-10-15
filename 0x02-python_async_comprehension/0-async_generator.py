#!/usr/bin/env python3
"""
A module containing an async generator function that yields
a random float between 0 and 10 every second, 10 times.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Coroutine that yields a random float between 0 and 10
    every second for 10 iterations.

    Yields:
        float: Random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)