# https://www.hackerrank.com/challenges/count-triplets-1/problem
from collections import Counter

import pytest


def count_tripes(iterable, ratio):
    frequencies = Counter(iterable)
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

    ]

)
def test_answers(ratio, expected, iterable):
    assert count_tripes(iterable, ratio) == expected
