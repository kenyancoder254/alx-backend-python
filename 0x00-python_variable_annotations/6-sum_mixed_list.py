#!/usr/bin/env python3
"""Annotates a list of mixed integers and floats"""
from typing import List, Union


def sum_mixed_list(sum_mixed_list: List[Union[int, float]]) -> float:
    """Returns the sum of mixed integers and floats in a list"""
    result: float = sum([item for item in sum_mixed_list])
    return result
