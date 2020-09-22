from typing import List

import pytest


def find_runner_up(n: int, scores: List[int]) -> int:
    if len(scores) < 2:
        raise Exception()
    sorted_scores = sorted(scores, reverse=True)
    champion = sorted_scores[0]
    for score in sorted_scores:
        if score < champion:
            return score
    raise Exception()


@pytest.mark.parametrize(
    'expected,n,scores',
    [
        (
                5,
                5,
                [2, 3, 6, 6, 5]
        )
    ]
)
def test_find_runner_up(expected, n, scores):
    assert find_runner_up(n, scores) == expected


@pytest.mark.parametrize(
    'n,scores',
    [
        (0, []),
        (1, [1]),
    ]
)
def test_less_then_two_runner(n, scores):
    with pytest.raises(Exception):
        find_runner_up(n, scores)


def test_all_champions():
    with pytest.raises(Exception):
        find_runner_up(10, [10] * 10)
