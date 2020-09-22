# http://www.programcreek.com/2014/06/leetcode-wildcard-matching-java/
import heapq


def match(word, pattern):
    if len(word) != len(pattern):
        return False
    wilds = set('?*')
    for c, c2 in zip(word, pattern):
        if c2 not in wilds and c != c2:
            return False
    return True


import unittest


class Test(unittest.TestCase):
    def test_fail(self):
        self.assertFalse(match('aab', 'aaa'))

    def test_diff_len(self):
        self.assertFalse(match('aab', 'aabb'))

    def test_success(self):
        self.assertTrue(match('aab', 'aab'))
        self.assertTrue(match('aab', '*ab'))
        self.assertTrue(match('aab', '?ab'))

heapq.merge()
