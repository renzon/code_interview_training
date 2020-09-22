# http://www.programcreek.com/2014/05/leetcode-minimum-size-subarray-sum-java/

import unittest

import math


def min_size_sub_array_sum(seq, sum_):
    min_len = float('inf')
    current_sum = seq[0]
    start = 0
    end = 0
    n = len(seq)
    while start < n:
        if current_sum >= sum_:
            min_len = min(min_len, end - start + 1)
            if min_len == 1:
                return 1
            current_sum -= seq[start]
            start += 1
        else:
            end += 1
            if end == n:
                break
            current_sum += seq[end]

    return min_len if math.isfinite(min_len) else 0


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(2, min_size_sub_array_sum([2, 3, 1, 2, 4, 3], 7))
        self.assertEquals(6, min_size_sub_array_sum([2, 3, 1, 2, 4, 3], 15))
        self.assertEquals(0, min_size_sub_array_sum([2, 3, 1, 2, 4, 3], 16))
        self.assertEquals(1, min_size_sub_array_sum([2, 3, 1, 2, 4, 3], 2))
