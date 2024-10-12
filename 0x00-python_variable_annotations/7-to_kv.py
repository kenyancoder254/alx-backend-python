#!/usr/bin/env python3
"""Uses function annotation"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple"""
    my_tuple: Tuple[str, float] = (k, (v * v))
    return my_tuple
