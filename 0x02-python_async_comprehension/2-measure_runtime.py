#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times
       in parallel using asyncio.gather."""
    start = time.time()
    task_times = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task_times)
    end = time.time()
    total_time = end - start

    return total_time
