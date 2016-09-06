# First Approach
from collections import deque

import pytest


def max_slide(seq, k):
    if k == 0:
        return []
    window = deque(maxlen=k)
    result = []
    for elt in seq:
        window.append(elt)
        result.append(max(window))
    while True:
        window.popleft()
        if window:
            result.append(max(window))
        else:
            break
    return result


pytest


def test_max_slide():
    assert [] == max_slide(range(3), 0)
    assert list(range(3)) == max_slide(range(3), 1)
    assert list(range(3)) + [2] == max_slide(range(3), 2)
