# http://www.programcreek.com/2013/01/leetcode-longest-consecutive-sequence-java/
# Solution need to run in O(n) complexity, so sorting isn't an option

import unittest


def longest(iterable):
    nums = set(iterable)
    min_ = 0
    max_ = 0
    while len(nums) > (max_ - min_):
        maybe_min = next(iter(nums))  # pick a number from set
        maybe_max = maybe_min + 1
        # find consecutive minor integers until it is not on set.
        while maybe_min in nums:
            nums.remove(maybe_min)
            maybe_min -= 1

        maybe_min += 1  # keeping interval closed on beginning

        # find consecutive greater integers until it is not on set.
        while maybe_max in nums:
            nums.remove(maybe_max)
            maybe_max += 1
        if (maybe_max - maybe_min) > (max_ - min_):
            max_ = maybe_max
            min_ = maybe_min

    return range(min_, max_)


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(range(1, 5), longest([100, 4, 200, 1, 3, 2]))
        self.assertEquals(range(0), longest([]))
        self.assertEquals(range(1, 2), longest([1]))
