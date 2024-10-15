#!/usr/bin/env python3
"""Async Comprehensions module."""

from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension."""
    return [i async for i in async_generator()]