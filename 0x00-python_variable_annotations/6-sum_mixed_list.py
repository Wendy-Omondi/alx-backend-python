#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of integers and float and
       returns their sum as floats"""
    return sum(mxd_lst)
