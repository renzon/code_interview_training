# http://www.programcreek.com/2014/02/leetcode-find-peak-element/

import unittest
from itertools import chain, islice


def peak(seq):
    extreme = (float('-inf'),)
    left_seq = chain(extreme, seq)
    right_seq = chain(islice(seq, 1, None), extreme)
    for i, (left, middle, right) in enumerate(zip(left_seq, seq, right_seq)):
        if middle > left and middle > right:
            return i


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(0, peak([1]))
        self.assertEquals(1, peak([1, 2]))
        self.assertEquals(2, peak([1, 2, 3, 1]))
        self.assertEquals(4, peak([1, 2, 3, 8, 9, 8, 1]))
