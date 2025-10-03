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
    (0, 2)
    >>> two_sum([1, 3, 8], 2)
    Traceback (most recent call last):
        ...
    ValueError: No solution found
    >>> two_sum([1, 3, 8, 1], 2)
    (0, 3)
    >>> two_sum([2,7,11,15], 9)
    (0, 1)
    """

    # Solution O(n) in time and memory

    n = len(nums)
    if n <= 1:
        raise MinLenException(f'nums must have at least to elements, but has {n}')
    index_map={}
    for idx, num in enumerate(nums):
        indexes = index_map.get(num, [])
        indexes.append(idx)
        index_map[num] = indexes
    for num, indexes in index_map.items():
        complement = target - num
        if complement in index_map:
            if complement != num:
                return indexes[0], index_map[complement][0]
            elif len(indexes) >= 2:
                return indexes[0], indexes[1]
    raise ValueError('No solution found')

