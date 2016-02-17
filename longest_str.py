# http://www.programcreek.com/2013/02/leetcode-longest-substring-without-repeating-characters-java/
import unittest


def longest(s):
    longest_s = []
    read_chars = set()
    current = []
    for char in s:
        if char in read_chars:
            if len(current) > len(longest_s):
                longest_s = list(current)
            read_chars.clear()
            current.clear()
        current.append(char)
        read_chars.add(char)
    return ''.join(max(longest_s, current, key=len))


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals('abc', longest('abcabcbb'))
