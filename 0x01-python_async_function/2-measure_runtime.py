#!/usr/bin/env python3
import time
import asyncio
from typing import List
import importlib.util

# Dynamically import the '0-basic_async_syntax.py' file to access wait_random
module_name = 'wait_random_module'
spec = importlib.util.spec_from_file_location(module_name, './0-basic_async_syntax.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Call the wait_n function
    total_time = time.time() - start_time  # Calculate the elapsed time
    return total_time / n  # Return the average time per task
