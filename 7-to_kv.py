#!/usr/bin/env python3
"""
Function that returns a tuple containing a string and the square of an int or float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string and the second element is the square of the int or float.
    """
    return (k, float(v ** 2))
