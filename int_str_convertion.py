from collections import deque
from unittest.case import TestCase


def to_int(number_str):
    negative_flag = False
    n = 0
    for char in number_str:
        if char == '-':
            negative_flag = True
        elif char != '+':
            n *= 10
            n += int(char)
    if negative_flag:
        return -n
    return n


def to_str(n):
    if n == 0:
        return '0'
    abs_n = abs(n)
    buffer = deque()
    while abs_n != 0:
        buffer.appendleft(str(abs_n % 10))
        abs_n //= 10
    if n < 0:
        buffer.appendleft('-')
    return ''.join(buffer)


class ConvertionTests(TestCase):
    def test_to_int(self):
        self.assertEqual(1234567890, to_int('1234567890'))
        self.assertEqual(-1234567890, to_int('-1234567890'))

    def test_to_str(self):
        self.assertEqual('1234567890', to_str(1234567890))
        self.assertEqual('-1234567890', to_str(-1234567890))

