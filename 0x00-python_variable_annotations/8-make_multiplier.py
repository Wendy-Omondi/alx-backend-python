#!/usr/bin/env python3
""" type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """that takes a float multiplier as argument and
       returns a function that multiplies a float by multiplier."""
    def function(n: float):
        return n * multiplier
    return function
