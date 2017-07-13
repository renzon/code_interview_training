from collections import Counter

import pytest


def find_pair_with_sum(seq, pair_sum):
    """Find a pair (a, b) in seq for which a + b is equals to pair_sum
    Returns the pair if it exists or None otherwise

    :param seq: a sequence
    :param pair_sum: int with pair some
    :return: tuple with pair or None
    """
    elements = Counter(seq)
    for e, freq in elements.items():
        candidate = pair_sum - e
        if (candidate == e and freq >= 2) or (
                candidate != e and candidate in elements):
            return e, candidate


@pytest.mark.parametrize(
    'pair_sum,seq,expected',
    [
        (199, range(101), (100, 99)),
        (1, range(101), (0, 1)),
        (4, [2, 3, 2], (2, 2)),
    ]
)
def test_positive_pair_sum(pair_sum, seq, expected):
    assert sorted(expected) == sorted(find_pair_with_sum(seq, pair_sum))


@pytest.mark.parametrize(
    'pair_sum,seq',
    [
        (200, range(101)),
        (0, range(101)),
        (4, [2, 3])
    ]
)
def test_negative_pair_sum(pair_sum, seq):
    assert find_pair_with_sum(seq, pair_sum) is None
