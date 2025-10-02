# https://leetcode.com/problems/add-two-numbers/description/
from itertools import zip_longest
from typing import Iterable


def add_two_numbers(l1: Iterable[int], l2:Iterable[int]) -> Iterable[int]:
    """
    >>> add_two_numbers([10], [0])
    Traceback (most recent call last):
        ...
    ValueError: digits must be between 0 and 9, but got 10 and 0
    >>> add_two_numbers([0], [0])
    [0]
    >>> add_two_numbers([1], [0])
    [1]
    >>> add_two_numbers([1], [9])
    [0, 1]
    >>> add_two_numbers([1], [9, 9])
    [0, 0, 1]

    """
    # O(max(len(l1), len(l2)) in time and memory
    carry = 0

    def add_two_digitis(d1:int, d2: int) -> int:
        nonlocal carry
        if not (0<= d1 <= 9) or not (0<= d2 <= 9):
            raise ValueError(f'digits must be between 0 and 9, but got {d1} and {d2}')
        carry, digit = divmod(d1 + d2 + carry, 10)
        return digit

    sum_list=[add_two_digitis(d1, d2) for d1, d2 in zip_longest(l1, l2, fillvalue=0)]
    if carry:
        sum_list.append(carry)
    return sum_list
