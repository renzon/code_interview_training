# https://leetcode.com/problems/two-sum/
from collections import Counter
from typing import List, Tuple


class MinLenException(Exception):
    pass


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    >>> two_sum([], 9)
    Traceback (most recent call last):
        ...
    two_sum.MinLenException: nums must have at least to elements, but has 0
    >>> two_sum([1], 9)
    Traceback (most recent call last):
        ...
    two_sum.MinLenException: nums must have at least to elements, but has 1
    >>> two_sum([1, 3, 8], 9)
    (1, 8)
    >>> two_sum([1, 3, 8], 2)
    Traceback (most recent call last):
        ...
    ValueError: No solution found
    >>> two_sum([1, 3, 8, 1], 2)
    (1, 1)
    """

    # Solution O(n) in time and memory

    n = len(nums)
    if n <= 1:
        raise MinLenException(f'nums must have at least to elements, but has {n}')
    frequencies = Counter(nums)
    for num, freq in frequencies.items():
        complement = target - num
        if complement in frequencies:
            if complement != num or freq > 1:
                return num, complement
    raise ValueError('No solution found')

