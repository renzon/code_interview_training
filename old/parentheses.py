# http://www.programcreek.com/2012/12/leetcode-valid-parentheses-java/
import unittest


def parentheses(exp):
    stack = []
    signs = {'(': ')', '{': '}', '[': ']'}
    for c in exp:
        if c in signs:
            stack.append(c)
        else:
            try:
                open_sign = stack.pop()
            except IndexError:
                return False
            else:
                if c != signs[open_sign]:
                    return False
    return len(stack) == 0


class Test(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(parentheses('({[]})'))

    def test_invalid(self):
        self.assertFalse(parentheses('({[]}))'))
        self.assertFalse(parentheses('({[])}'))
