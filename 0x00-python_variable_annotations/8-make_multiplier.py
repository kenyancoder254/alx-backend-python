#!/usr/bin/env python3
"""python annotation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float"""
    def multiply(number: float) -> float:
        """Multipies number by float"""
        return number * multiplier
    return multiply
