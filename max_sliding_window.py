# First Approach
from collections import deque


def max_slide(seq, k):
    """Calculate de max slide window

    running time O(k(k+1) + (n-2k)*k) if n>=k

    :param seq: a sequence
    :param k: a int
    :return: max sliding window
    """
    if k <= 0:
        return []
    window = deque(maxlen=k)
    result = []
    for elt in seq:
        window.append(elt)
        result.append(max(window))
    while window:
        window.popleft()
        if window:
            result.append(max(window))
        else:
            break
    return result




def test_max_slide():
    assert [] == max_slide(range(3), 0)
    assert [] == max_slide([], 3)
    assert list(range(3)) == max_slide(range(3), 1)
    assert list(range(3)) + [2] == max_slide(range(3), 2)
