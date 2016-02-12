# http://www.programcreek.com/2013/01/leetcode-valid-palindrome-java/
import unittest


def is_palindrome(s):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_palindrome('Red rum, sir, is murder'))
        self.assertFalse(is_palindrome('Programcreek is awesome'))
