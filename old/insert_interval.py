# problem
import operator
from bisect import bisect
from unittest.case import TestCase


def insert(intervals, interval):
    """
    log(n) solution. instervals must be sorted by start
    :param intervals: sorted by start intervals
    :param interval:
    :return:
    """

    class NotMerged(Exception):
        pass

    def merge(i, i2):
        s, e = i
        s2, e2 = i2
        if s2 <= e:
            return s, max(e, e2)
        raise NotMerged()

    insert_position = bisect(list(map(operator.itemgetter(0), intervals)), interval[0])
    previous = insert_position - 1

    yield from (intervals[j] for j in range(previous))  # return item left from previous

    curr_start, curr_end = interval
    if previous >= 0:
        try:
            curr_start, curr_end = merge(intervals[previous], interval)
        except NotMerged:
            yield intervals[previous]

    for i in range(insert_position, len(intervals)):
        try:
            curr_start, curr_end = merge((curr_start, curr_end), intervals[i])
        except NotMerged:
            yield curr_start, curr_end
            break  # If merge does not ocurr whe only need returns item start from i to end without merging

    yield from (intervals[j] for j in range(i, len(intervals)))


class Test(TestCase):
    def test(self):
        self.assertTupleEqual(((1, 5), (6, 9)), tuple(insert([(1, 3), (6, 9)], (2, 5))))
        self.assertTupleEqual(((1, 2), (3, 10), (12, 16)),
                              tuple(insert([(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)], (4, 9))))
