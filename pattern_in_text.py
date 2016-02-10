# http://www.programcreek.com/2012/12/leetcode-implement-strstr-java/
import unittest


def search(pattern, text):
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


class Test(unittest.TestCase):
    def test_char(self):
        self.assertEqual(0, search('a', 'abacate'))

    def test_begin(self):
        self.assertEqual(0, search('ab', 'abacate'))

    def test_middle(self):
        self.assertEqual(2, search('ac', 'abacate'))

    def test_final(self):
        self.assertEqual(5, search('te', 'abacate'))
