# http://www.programcreek.com/2014/02/leetcode-find-minimum-in-rotated-sorted-array/

import unittest

from itertools import islice


def my_min(seq):
    if seq:
        for v, next_v in zip(seq, islice(seq, 1, None)):
            if next_v < v:
                return next_v
        return seq[0]


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(0, my_min(tuple(range(9))))
        self.assertEquals(0, my_min(tuple(range(5, 9)) + tuple(range(5))))
        self.assertEquals(0, my_min(tuple(range(1, 9)) + tuple(range(1))))
