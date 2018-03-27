from math import inf

import pytest


def max_stock_profit(series):
    """Calculate maximum profit from a temporal series, return a tuple where first element is the min
    value which occurred before the max value, the second element

    :param series: list
    :return: tuple (min, max)
    """
    if len(series) < 2:
        raise ValueError("series must have at least two values")
    iterable = iter(series)
    max_profit = max_point = -inf
    min_point = aux_min_point = next(iterable)
    for current_point in iterable:
        current_profit = current_point - aux_min_point
        if current_profit >= max_profit:
            max_profit = current_profit
            max_point = current_point
            min_point = min(aux_min_point, min_point)
        aux_min_point = min(aux_min_point, current_point)

    return min_point, max_point


@pytest.mark.parametrize(
    'series, expected',
    [
        ([10, 7, 5, 4, 8, 11, 9, 4], (4, 11)),
        ([10, 7, 5, 4], (5, 4)),
        ([11, 11, 10, 10, 8], (10, 10))
    ]
)
def test(series, expected):
    assert max_stock_profit(series) == expected
