def calc(expression):
    if not expression:
        return 0
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '/': lambda a, b: a // b,
           '*': lambda a, b: a * b}
    stack = []
    for op in expression.split(' '):
        try:
            n = int(op)
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            n = ops[op](a, b)
        stack.append(n)
    return stack.pop()


import unittest


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(3, calc('1 2 +'))
        self.assertEqual(6, calc('4 13 5 / +'))


