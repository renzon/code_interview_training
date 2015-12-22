NUMBER_TO_ALPHA = ['WYZ', 'ABC', 'DEF']


def generate_alpha(number_sequence):  # number_sequence = '1'
    return recursive_version(number_sequence)


def _rec(result, digits, idx=0):
    if idx == len(digits):
        yield result
    else:
        d = digits[idx]
        for choice in NUMBER_TO_ALPHA[d]:
            next_result = result + (choice,)
            yield from _rec(next_result, digits, idx + 1)


def recursive_version(number_sequence):
    digits = tuple(map(lambda i: int(i), number_sequence))

    return [''.join(p) for p in _rec(tuple(), digits)]


import unittest


class GenerateAlpha(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([''], generate_alpha(''))

    def test_items_number(self):
        self.assertEqual(1, len(generate_alpha('')))
        self.assertEqual(3, len(generate_alpha('1')))
        self.assertEqual(9, len(generate_alpha('12')))
        self.assertEqual(27, len(generate_alpha('121')))

    def test_simple_case(self):
        self.assertEqual(['A', 'B', 'C'], generate_alpha('1'))
        self.assertIn('AA', generate_alpha('11'))

    def test_item_length(self):
        self.assertEqual(1, len(generate_alpha('1')[0]))
        self.assertEqual(2, len(generate_alpha('12')[0]))
        self.assertEqual(3, len(generate_alpha('121')[0]))
