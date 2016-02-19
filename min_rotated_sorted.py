# http://www.programcreek.com/2014/02/leetcode-find-minimum-in-rotated-sorted-array/

import unittest


def my_min(seq):
    if seq:
        lo = 0
        hi = len(seq)

        while lo < (hi - 2):
            middle = (lo + hi) // 2
            lo_value = seq[lo]
            middle_value = seq[middle]
            hi_value = seq[hi - 1]

            if lo_value <= middle_value <= hi_value:
                return lo_value
            elif middle_value < lo_value:
                hi = middle + 1
            else:
                lo = middle + 1
        return min(seq[lo], seq[hi - 1])


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(0, my_min(tuple(range(9))))
        self.assertEquals(0, my_min(tuple(range(5, 9)) + tuple(range(5))))
        self.assertEquals(0, my_min(tuple(range(1, 9)) + tuple(range(1))))
        self.assertEquals(1, my_min([5, 1, 1, 1, 3, 4]))
