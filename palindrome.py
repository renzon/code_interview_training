# http://www.programcreek.com/2013/01/leetcode-valid-palindrome-java/
import unittest


def is_palindrome(s):
    s = tuple(map(str.lower, filter(str.isalpha, s)))
    return s == tuple(reversed(s))


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_palindrome('Red rum, sir, is murder'))
        self.assertFalse(is_palindrome('Programcreek is awesome'))
