# http://www.programcreek.com/2012/12/leetcode-implement-strstr-java/
import unittest


def search_naive(pattern, text):
    """
    pattern matching with O(nm) time complexity where n=len(text) and m=len(pattern)
    :param pattern:
    :param text:
    :return:
    """
    start = 0

    def remaining(start_):
        yield from (text[i] for i in range(start_, len(text)))

    while len(pattern) <= len(text) - start:
        for c, c2 in zip(pattern, remaining(start)):
            if c != c2:
                start += 1
                break
        else:
            return start
    return -1


def search(pattern, text):
    """
    KMP algorithm with O(n+m) time complexity
    :param pattern:
    :param text:
    :return:
    """
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    def calc_fail():
        fail = [0] * m
        i = 0
        j = 1
        while j < m:
            if pattern[i] == pattern[j]:
                fail[j] = fail[j - 1] + 1
                j += 1
                i += 1
            elif i > 0:
                i = fail[i - 1]
            else:
                j += 1
        return fail

    fail = calc_fail()

    i = 0
    j = 0
    while (n - i) >= (m - j):
        if pattern[j] == text[i]:
            if j == (m - 1):
                return i - j
            i += 1
            j += 1
        elif j > 0:
            j = fail[j - 1]
        else:
            j = 0
            i += 1

    return -1


#
# i = 3
# j = 1
# acab

print(search('amalgamation', ''))


class Test(unittest.TestCase):
    def test_char(self):
        self.assertEqual(0, search('a', 'abacate'))

    def test_begin(self):
        self.assertEqual(0, search('ab', 'abacate'))

    def test_middle(self):
        self.assertEqual(2, search('ac', 'abacate'))

    def test_final(self):
        self.assertEqual(5, search('te', 'abacate'))
