#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""


import asyncio, random
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """returns list in ascending order because of concurrence"""
    delays_list: List[float] = []
    delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delays in asyncio.as_completed((delays)):
        listed = await delays
        delays_list.append(listed)
    return delays_list
