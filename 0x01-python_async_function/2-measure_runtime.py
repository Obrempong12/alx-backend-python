#!/usr/bin/env python3

"""
Task details:

From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time func with integers `n` and `max_delay` as arguments
that measures the total execution time for `wait_n(n, max_delay)`, and returns
`total_time / n`. Your func should return a float.

Use the `time` module to measure an approximate elapsed time.
"""

import asyncio
from time import time
from typing import Callable

wait_n: Callable = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This func returns the average time for `wait_n(n, max_delay)` to
    execute.
    """

    start_time: float = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - start_time) / n
