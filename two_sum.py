# Problem http://www.programcreek.com/2012/12/leetcode-solution-of-two-sum-in-java/
from bisect import bisect, bisect_left
from unittest.case import TestCase


class NotFound(Exception):
    pass


def two_sum(ints, sum):
    n = len(ints)
    ints = sorted(ints)
    end = n
    start = 0

    while start < end:
        wanted = sum - ints[start]
        previous = bisect(ints, wanted, start, end) - 1
        if previous >= 0 and wanted == ints[previous] and start != previous:
            return start + 1, previous + 1
        start = max(start + 1, bisect_left(ints, sum - ints[end - 1], start + 1, previous + 1) - 1)
        end = previous + 1

    raise NotFound()


class Tests(TestCase):
    def test_empty_input(self):
        self.assertRaises(NotFound, two_sum, [], 0)

    def test_single_n(self):
        self.assertRaises(NotFound, two_sum, [1], 0)

    def test_sum_less_then_min(self):
        self.assertRaises(NotFound, two_sum, [1, 2], 0)

    def test_sum_greater_then_max(self):
        self.assertRaises(NotFound, two_sum, [1, 2], 4)

    def test_obvious_case(self):
        self.assertEquals((1, 2), two_sum([3, 2], 5))

    def test_middle(self):
        self.assertEquals((7, 10), two_sum(range(10), 15))

    def test_repeated(self):
        self.assertEquals((2, 3), two_sum([0, 2, 2], 4))

    def test_trick_when_sum_minus_element_equals_to_element(self):
        self.assertRaises(NotFound, two_sum, [0, 4], 0)

    def test_not_found(self):
        self.assertRaises(NotFound, two_sum, [1, 10], 1)
