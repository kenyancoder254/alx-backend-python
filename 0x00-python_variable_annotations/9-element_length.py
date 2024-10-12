#!/usr/bin/env python3
"""Annotate function's parameters"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Annotates a function"""
    return [(i, len(i)) for i in lst]
