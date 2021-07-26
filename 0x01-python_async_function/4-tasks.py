#!/usr/bin/env python3
"""alter wait_n code into a new function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """returns list in ascending order because of concurrence"""
    delays_list: List[float] = []
    delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delays in asyncio.as_completed((delays)):
        listed = await delays
        delays_list.append(listed)
    return delays_list
