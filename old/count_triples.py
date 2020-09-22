# https://www.hackerrank.com/challenges/count-triplets-1/problem
import operator as op
from collections import Counter
from functools import reduce

import pytest


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def count_tripes(iterable, ratio):
    frequencies = Counter(iterable)
    if ratio == 1:
        total = 0
        for i, freq in frequencies.items():
            if freq > 2:
                total += ncr(freq, 3)

        return total

    total = 0
    for first, first_freq in frequencies.items():
        second = first * ratio
        if second not in frequencies:
            continue
        third = second * ratio
        if second not in frequencies:
            continue
        total += first_freq * frequencies[second] * frequencies[third]
    return total


@pytest.mark.parametrize(
    ' ratio, expected, iterable',
    [
        (2, 2, [1, 2, 2, 4]),
        (3, 6, [1, 3, 9, 9, 27, 81]),
        (1, 5, [1, 1, 1, 1, 3, 3, 3]),

    ]

)
def test_answers(ratio, expected, iterable):
    assert count_tripes(iterable, ratio) == expected
