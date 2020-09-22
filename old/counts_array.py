from itertools import islice
from typing import List


def counts_array(lst: List) -> List:
    counts = []
    for i, value in enumerate(lst):
        counts.append(0)
        for j, left_value in enumerate(islice(lst, 0, i)):
            if value < left_value:
                counts[j] += 1
    return counts


def test_counts():
    assert counts_array([4, 3, 2, 1, 4]) == [3, 2, 1, 0, 0]
