# http://www.programcreek.com/2014/06/leetcode-longest-valid-parentheses-java/
import unittest


def parentheses(exp):
    def remaining_elements(start):
        return ((i, exp[i]) for i in range(start, len(exp)))

    start = 0
    longest = []
    stack = []
    current = []

    while start < len(exp):
        for i, char in remaining_elements(start):
            current.append(char)
            if char == '(':
                stack.append(char)
            else:
                try:
                    stack.pop()
                except IndexError:
                    start += 1
                    current.clear()
                    break
                else:
                    if len(stack) == 0 and len(current) > len(longest):
                        longest = list(current)
                        start = i
        else:
            if not stack:
                start += 1
                current.clear()
                stack.clear()

    return ''.join(longest)


class Test(unittest.TestCase):
    def test_valid(self):
        self.assertEqual('(())', parentheses('(())'))

    def test_invalid_on_right(self):
        self.assertEqual('()', parentheses('())'))

    def test_invalid_on_right_and_lkeft(self):
        self.assertEqual('()()', parentheses(')()())'))
