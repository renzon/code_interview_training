# use of int to parse is not allowed. Way of doing count with big number which could cause overflow on other languages
import unittest
from itertools import zip_longest


def reversed_int_digits(s):
    return map(int, reversed(s))


def bynary_sum(n, n2):
    remainder = 0
    reversed_result = []
    for d, d2 in zip_longest(reversed_int_digits(n), reversed_int_digits(n2), fillvalue=0):
        sum_ = remainder + d + d2
        reversed_result.append(str(sum_ % 2))
        remainder = 0 if sum_ < 2 else 1
    if remainder == 1:
        reversed_result.append('1')
    return ''.join(reversed(reversed_result))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual('10110', bynary_sum('1010', '1100'))
        self.assertEqual('100110', bynary_sum('11010', '1100'))
