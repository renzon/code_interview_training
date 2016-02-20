# http://www.programcreek.com/2014/02/leetcode-find-peak-element/

import unittest

minus_inf = float('-inf')


class ExtremesMinusInf():
    def __init__(self, seq):
        self.seq = seq
        self.seq_len = len(seq)

    def __getitem__(self, i):
        if i == -1 or i == self.seq_len:
            return minus_inf
        return self.seq[i]


def peak(seq):
    if seq:
        proxy = ExtremesMinusInf(seq)
        lo = 0
        hi = len(seq)
        while lo < hi:
            middle = (hi + lo) // 2
            left = proxy[middle - 1]
            right = proxy[middle + 1]
            possible_peak = proxy[middle]
            if left <= possible_peak and right <= possible_peak:
                return middle
            elif left > possible_peak:
                hi = middle
            else:
                lo = middle + 1
        return lo


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(0, peak([1]))
        self.assertEquals(1, peak([1, 2]))
        self.assertEquals(2, peak([1, 2, 3, 1]))
        self.assertEquals(4, peak([1, 2, 3, 8, 9, 8, 1]))
