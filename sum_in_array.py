# Geralising the problem http://www.programcreek.com/2013/02/leetcode-4sum-java/ for n sum
# Difference: this method return 0-based indexes
from itertools import combinations
from unittest import TestCase


class NotFound(Exception):
    pass


def any_sum(numbers, r, summ):  # summ with two "m" letters to avoid conflict with builtin
    n = len(numbers)

    for c in combinations(range(n), r):
        if sum(numbers[i] for i in c) == summ:
            return c

    raise NotFound()


class Tests(TestCase):
    def test_empty_input(self):
        self.assertRaises(NotFound, any_sum, [], 2, 0)

    def test_single_n(self):
        self.assertRaises(NotFound, any_sum, [1], 2, 0)

    def test_sum_less_then_min(self):
        self.assertRaises(NotFound, any_sum, [1, 2], 2, 0)

    def test_sum_greater_then_max(self):
        self.assertRaises(NotFound, any_sum, [1, 2], 2, 4)

    def test_obvious_case(self):
        self.assertEquals((0, 1), any_sum([2, 3], 2, 5))

    def test_middle(self):
        self.assertEquals((6, 9), any_sum(range(10), 2, 15))

    def test_repeated(self):
        self.assertEquals((1, 2), any_sum([0, 2, 2], 2, 4))

    def test_trick_for_bysect_right_and_left(self):
        self.assertRaises(NotFound, any_sum, [2, 2, 2, 2, 2], 2, 5)

    def test_trick_when_sum_minus_element_equals_to_element(self):
        self.assertRaises(NotFound, any_sum, [0, 4], 2, 0)

    def test_not_found(self):
        self.assertRaises(NotFound, any_sum, [1, 10], 2, 1)
