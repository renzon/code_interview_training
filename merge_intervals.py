from itertools import islice
from unittest.case import TestCase


def merge(intervals):
    intervals = sorted(intervals)
    n = len(intervals)
    if n == 0:
        return
    curr_start, curr_end = intervals[0]
    for start, end in islice(intervals, 1, None):
        if start <= curr_end:
            curr_end = max(curr_end, end)
        else:
            yield curr_start, curr_end
            curr_start, curr_end = start, end
    yield curr_start, curr_end


class Test(TestCase):
    def test(self):
        self.assertTupleEqual(((1, 6), (8, 10), (15, 18)), tuple(merge(((1, 3), (2, 6), (8, 10), (15, 18)))))
