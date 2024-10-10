#!/usr/bin/env python3
"""
Function that returns a list of tuples, each containing a sequence and its length.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
