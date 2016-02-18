# http://www.programcreek.com/2014/05/leetcode-minimum-window-substring-java/

import math
import unittest
from collections import Counter


def min_str(s, t):
    if s == '' and t == '':
        return ''

    counter = Counter(t)
    missing = set(counter.keys())
    min_start = 0
    min_end = float('inf')
    cursor_end = 0
    s_len = len(s)

    for cursor_start, char in enumerate(s):
        if missing:
            try:
                cursor_end = advance_window_end(counter, cursor_end, missing, s, s_len)
            except StopIteration:
                break

        if not missing:
            if (min_end - min_start) > (cursor_end - cursor_start):
                min_start = cursor_start
                min_end = cursor_end
            if char in counter:
                counter[char] += 1
                if counter[char] == 1:
                    missing.add(char)

    if math.isfinite(min_end):
        return s[min_start:min_end]
    raise Exception()


def advance_window_end(counter, cursor_end, missing, s, s_len):
    for cursor_end in range(cursor_end, s_len):
        end_char = s[cursor_end]
        if end_char in counter:
            counter[end_char] -= 1
            if counter[end_char] == 0:
                missing.remove(end_char)
                if not missing:
                    return cursor_end + 1  # keeping open interval
    raise StopIteration()


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals('BANC', min_str('ADOBECODEBANC', 'ABC'))

    def test_all_empty(self):
        self.assertEquals('', min_str('', ''))

    def test_empty_t(self):
        self.assertEquals('', min_str('abc', ''))

    def test_error(self):
        self.assertRaises(Exception, min_str, 'abc', 'd')
