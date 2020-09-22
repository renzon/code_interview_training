# Problem: http://www.programcreek.com/2012/12/leetcode-string-to-integer-atoi/
# Obviously int builtin can not be used

import re
from functools import reduce
from itertools import islice
from unittest.case import TestCase

digit_converter = {str(i): i for i in range(10)}


def to_int(s):
    m = re.fullmatch(r'[+-]?(\d+)', s)
    if not m:
        raise ValueError()
    digits = map(digit_converter.get, m.group(1))

    def accumulate(sum_, digit):
        return 10 * sum_ + digit

    result = reduce(accumulate, digits, 0)
    return result if s[0] != '-' else -result


class Test(TestCase):
    def assertNumber(self, s):
        self.assertEquals(int(s), to_int(s))

    def assertRaisesNumber(self, s):
        try:
            int(s)
        except Exception as e:
            exc_class = type(e)
            self.assertRaises(exc_class, to_int, s)

    def test_all_digitis(self):
        self.assertNumber(''.join(map(str, range(2, 11))))

    def test_invalid_chars(self):
        self.assertRaisesNumber('')
        self.assertRaisesNumber(' ')
        self.assertRaisesNumber(' 1')
        self.assertRaisesNumber(' 1b')
        self.assertRaisesNumber('1.1')
        self.assertRaisesNumber('1,100')

    def test_signed(self):
        self.assertNumber('+9')
        self.assertNumber('-9')
