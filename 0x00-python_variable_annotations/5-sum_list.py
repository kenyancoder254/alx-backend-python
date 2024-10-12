#!/usr/bin/env python3
"""Use of list annotations"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Finds the sum of floats in a list"""
    result: float = sum([item for item in input_list])
    return result
