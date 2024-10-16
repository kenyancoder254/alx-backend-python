#!/usr/bin/env python3
"""Implementation of async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay"""
    random_delay = random.uniform(0, max_delay)
    return random_delay
