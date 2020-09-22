from collections import defaultdict
from unittest.case import TestCase


def first_not_repeated_char(word):
    frequency_dct = defaultdict(lambda: 0)
    for char in word:
        frequency_dct[char] += 1
    for char in word:
        if frequency_dct[char] == 1:
            return char


class FirstNotRepeaterTests(TestCase):
    def test(self):
        self.assertEqual('o', first_not_repeated_char('o'))
        self.assertEqual('o', first_not_repeated_char('total'))