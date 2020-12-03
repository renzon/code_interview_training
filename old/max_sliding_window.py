# http://www.programcreek.com/2014/05/leetcode-sliding-window-maximum-java/

# First Approach
from collections import deque
from itertools import islice


def max_slide(seq, k):
    """Calculate de max slide window

    running time O(k-1+(n-k+1)*k) => O(nk+k**2)

    :param seq: a_com_fatia_linar sequence
    :param k: a_com_fatia_linar int
    :return: max sliding window
    """
    n = len(seq)
    if k <= 0 or k > n:
        return []
    iterable = iter(seq)
    window = deque(islice(iterable, k - 1))
    result = []
    for elt in iterable:
        window.append(elt)
        result.append(max(window))
    return result


def test_max_slide():
    assert_max_slide(max_slide)


def assert_max_slide(strategy):
    assert [] == strategy(range(3), 0)
    assert [] == strategy([], 3)
    assert list(range(3)) == strategy(range(3), 1)
    assert [1, 2] == strategy(range(3), 2)
    assert [3, 3, 5, 5, 6, 7] == strategy([1, 3, -1, -3, 5, 3, 6, 7], 3)
