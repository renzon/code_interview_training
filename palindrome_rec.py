from unittest.case import TestCase


def _is_palindrome_recursive(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return _is_palindrome_recursive(s, start + 1, end - 1)


def is_palindrome(s):
    start = 0
    end = len(s) - 1
    return _is_palindrome_recursive(s, start, end)


class PalindromeTest(TestCase):
    def test_empyt_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindromes(self):
        self.assertTrue(is_palindrome('A'))
        self.assertTrue(is_palindrome('AA'))
        self.assertTrue(is_palindrome('ABA'))
        self.assertTrue(is_palindrome('ABBA'))
        self.assertTrue(is_palindrome('ABCBA'))

    def test_not_palindromes(self):
        self.assertFalse(is_palindrome('AB'))
        self.assertFalse(is_palindrome('ABB'))
        self.assertFalse(is_palindrome('ABBB'))
        self.assertFalse(is_palindrome('ABAB'))
        self.assertFalse(is_palindrome('ABBAB'))
