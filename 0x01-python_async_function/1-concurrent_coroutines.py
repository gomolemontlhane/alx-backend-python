#!/usr/bin/env python3
import asyncio
from typing import List
import importlib.util

# Dynamically import the '0-basic_async_syntax.py' file
module_name = 'wait_random_module'
spec = importlib.util.spec_from_file_location(module_name, './0-basic_async_syntax.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of delays in ascending order.
    """
    # Create a list of asyncio tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Use asyncio.as_completed to process tasks as they complete
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    
    return delays
