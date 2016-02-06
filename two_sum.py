# Problem http://www.programcreek.com/2012/12/leetcode-solution-of-two-sum-in-java/
from unittest.case import TestCase


def two_sum(ints, sum):
    if len(ints) <= 1:
        raise ValueError()


class Tests(TestCase):
    def test_empty_input(self):
        self.assertRaises(ValueError, two_sum, [], 0)

    def test_single_n(self):
        self.assertRaises(ValueError, two_sum, [1], 0)
