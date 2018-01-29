from datetime import datetime, timedelta
from random import randint

import pytest

SATURDAY_DRAW_DATETIME = datetime(2018, 1, 27, 20)
FRIDAY_BEFORE_SATURDAY = datetime(2018, 1, 26, 20)
THURSDAY_BEFORE_SATURDAY = datetime(2018, 1, 25, 20)

WEDNESDAY_DRAW_DATETIME = datetime(2018, 1, 24, 20)
TUESDAY_BEFORE_WEDNESDAY = datetime(2018, 1, 23, 20)
MONDAY_BEFORE_WEDNESDAY = datetime(2018, 1, 22, 20)
SUNDAY_BEFORE_WEDNESDAY = datetime(2018, 1, 21, 20)

SATURDAY_WEEK_DAY = 5
WEDNESDAY_WEEK_DAY = 2
ONE_WEEK_TIME_DELTA = timedelta(days=7)


def calculate_next_draw(dt: datetime = None):
    dt = datetime.now() if dt is None else dt
    next_saturday_draw = _next_draw(SATURDAY_WEEK_DAY, dt)
    next_wednesday_draw = _next_draw(WEDNESDAY_WEEK_DAY, dt)
    return min(next_saturday_draw, next_wednesday_draw)


def _next_draw(draw_week_day, dt):
    week_day = dt.weekday()
    days_delta = draw_week_day - week_day
    if days_delta < 0:
        days_delta += 7
    next_draw = datetime(dt.year, dt.month, dt.day, 20) + timedelta(days=days_delta)
    if next_draw < dt:
        next_draw += ONE_WEEK_TIME_DELTA
    return next_draw


@pytest.mark.parametrize('dt', [WEDNESDAY_DRAW_DATETIME, SATURDAY_DRAW_DATETIME])
def test_exactly_draw_datetime(dt):
    assert dt == calculate_next_draw(dt)


@pytest.mark.parametrize('dt', [WEDNESDAY_DRAW_DATETIME, SATURDAY_DRAW_DATETIME, datetime.now()])
def test_draws_happens_in_the_future(dt):
    assert dt <= calculate_next_draw(dt)


def test_just_after_wednesday_draw():
    dt = WEDNESDAY_DRAW_DATETIME + timedelta(milliseconds=randint(1, 1000))
    assert SATURDAY_DRAW_DATETIME == calculate_next_draw(dt)


def test_just_before_wednesday_draw():
    dt = WEDNESDAY_DRAW_DATETIME + timedelta(milliseconds=randint(-1000, -1))
    assert WEDNESDAY_DRAW_DATETIME == calculate_next_draw(dt)


def test_just_after_saturday_draw():
    dt = SATURDAY_DRAW_DATETIME + timedelta(milliseconds=randint(1, 1000))
    assert (WEDNESDAY_DRAW_DATETIME + ONE_WEEK_TIME_DELTA) == calculate_next_draw(dt)


def test_just_before_saturday_draw():
    dt = SATURDAY_DRAW_DATETIME + timedelta(milliseconds=randint(-1000, -1))
    assert SATURDAY_DRAW_DATETIME == calculate_next_draw(dt)


@pytest.mark.parametrize('dt', [FRIDAY_BEFORE_SATURDAY, THURSDAY_BEFORE_SATURDAY])
def test_thursday_to_friday(dt):
    assert SATURDAY_DRAW_DATETIME == calculate_next_draw(dt)


@pytest.mark.parametrize(
    'dt',
    [SUNDAY_BEFORE_WEDNESDAY, MONDAY_BEFORE_WEDNESDAY, TUESDAY_BEFORE_WEDNESDAY]
)
def test_thursday_to_friday(dt):
    assert WEDNESDAY_DRAW_DATETIME == calculate_next_draw(dt)
