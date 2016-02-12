# http://www.programcreek.com/2013/01/leetcode-search-insert-position/


import unittest


def insert(seq, x, lo=0, hi=None):
    hi = len(seq) if hi is None else hi
    if hi == lo:
        return lo
    middle = (lo + hi) // 2
    element = seq[middle]
    if element == x:
        return middle
    elif element < x:
        return insert(seq, x, middle + 1, hi)
    else:
        return insert(seq, x, lo, middle)


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(2, insert([1, 3, 5, 6], 5))
        self.assertEquals(1, insert([1, 3, 5, 6], 2))
        self.assertEquals(4, insert([1, 3, 5, 6], 7))
        self.assertEquals(2, insert([1, 3, 5, 6], 4))
        self.assertEquals(0, insert([1, 3, 5, 6], 0))
