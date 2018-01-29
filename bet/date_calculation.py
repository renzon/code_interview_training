from datetime import datetime

import pytest

SATURDAY_DRAW_DATETIME = datetime(2018, 1, 27, 20)
WEDNESDAY_DRAW_DATETIME = datetime(2018, 1, 24, 20)


def calculate_next_draw(dt: datetime = None):
    dt = datetime.now() if dt is None else dt
    return dt


@pytest.mark.parametrize('dt', [WEDNESDAY_DRAW_DATETIME, SATURDAY_DRAW_DATETIME])
def test_exactly_draw_datetime(dt):
    assert dt == calculate_next_draw(dt)


@pytest.mark.parametrize('dt', [WEDNESDAY_DRAW_DATETIME, SATURDAY_DRAW_DATETIME, datetime.now()])
def test_draws_happens_in_the_future(dt):
    assert dt >= calculate_next_draw(dt)
