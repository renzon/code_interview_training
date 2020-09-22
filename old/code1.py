# First code of Toptal
# Find the sum of the digits of all the numbers from 1 to N (both ends included).#
# For N = 10 the sum is 1+2+3+4+5+6+7+8+9+(1+0) = 46
# For N = 11 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) = 48
from unittest import TestCase


def transform(n):
    sum = 0
    while n > 0:
        sum += (n % 10)
        n //= 10
    return sum


def sum_toptal(n):
    return sum(map(transform, range(1, n + 1)))


# N = 110
# sum = 957
#
# N = 90
# sum = 774

class Tests(TestCase):
    def test_digits_sum(self):
        self.assertEqual(1, transform(10))
        self.assertEqual(2, transform(11))
        self.assertEqual(3, transform(111))

    def test_10(self):
        self.assertEqual(46, sum_toptal(10))
        self.assertEqual(48, sum_toptal(11))
        self.assertEqual(51, sum_toptal(12))
        self.assertEqual(957, sum_toptal(110))
        self.assertEqual(774, sum_toptal(90))
