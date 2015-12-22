number_to_alpha = {'1': 'ABC', '2': 'DEF'}


def generate_alpha(number_sequence):  # number_sequence = '1'
    return recursive_version(number_sequence)


def recursive_version(number_sequence):
    if not number_sequence:
        return []
    idx = 0
    items = ['']

    def _generate_recursive(idx, items):  # idx = 0, items = ['']
        if idx == len(number_sequence):
            return items
        number = number_sequence[idx]  # number = '1'
        chars = number_to_alpha[number]  # chars = 'ABC'
        next_items = []  # ['A', 'B', 'C']
        for item in items:
            for c in chars:
                next_items.append(item + c)
        return _generate_recursive(idx + 1, next_items)

    return _generate_recursive(idx, items)


import unittest

class GenerateAlpha(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], generate_alpha(''))

    def test_items_number(self):
        self.assertEqual(0, len(generate_alpha('')))
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


