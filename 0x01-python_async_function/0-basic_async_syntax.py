#!/usr/bin/env python3
"""asynchronour coroutine - The basics of async"""
import asyncio
import random

async def wait_random(max_delay: int=10) -> float:
    """returns interger argument afer waiting 1 - 10 seconds"""
    integer = random.uniform(0, max_delay)
    await asyncio.sleep(integer)
    return integer
