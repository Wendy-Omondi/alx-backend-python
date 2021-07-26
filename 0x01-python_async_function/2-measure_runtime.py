#!/usr/bin/env python3
"""Measures an approximate elapsed time."""
import asyncio, time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total execution time"""
    start = time.time()
    asyncio.run(wait_n(max_delay, n))
    exec_time = time.time() - start
    total_time = exec_time / n

    return total_time
