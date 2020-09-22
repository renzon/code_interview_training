from itertools import cycle


def rotate(seq,k):
    seq_cycle=cycle(seq)
    for i in range(k):
        next(seq_cycle)
    for _,v in zip(range(len(seq)), seq_cycle):
        yield v


import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertListEqual([0,1,2,3,4],list(rotate(list(range(5)),0)))
        self.assertListEqual([1,2,3,4,0],list(rotate(list(range(5)),1)))
        self.assertListEqual([2,3,4,0,1],list(rotate(list(range(5)),2)))
        self.assertListEqual([3,4,0,1,2],list(rotate(list(range(5)),3)))

