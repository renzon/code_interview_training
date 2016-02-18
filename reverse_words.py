# http://www.programcreek.com/2014/02/leetcode-reverse-words-in-a-string-java/#

import unittest


def rev(words):
    return ' '.join(reversed(words.split(' ')))


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals("blue is sky the", rev("the sky is blue"))
