# http://www.programcreek.com/2014/06/leetcode-wildcard-matching-java/

def match(word, pattern):
    wilds = set('?*')
    for c, c2 in zip(word, pattern):
        if c2 not in wilds and c != c2:
            return False
    return True


import unittest


class Test(unittest.TestCase):
    def test_fail(self):
        self.assertFalse(match('aab', 'aaa'))

    def test_success(self):
        self.assertTrue(match('aab', 'aab'))
        self.assertTrue(match('aab', '*ab'))
        self.assertTrue(match('aab', '?ab'))


