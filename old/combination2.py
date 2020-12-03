def combination(sequence):
    def _recursive_combination(remaining_sequence, current_combination):
        for i, char in enumerate(remaining_sequence):
            new_combination = current_combination + char
            yield from _recursive_combination(remaining_sequence[:i] + remaining_sequence[i + 1:], new_combination)
        if not remaining_sequence and current_combination:
            yield current_combination
            combination

    return list(_recursive_combination(sequence, ''))


import unittest


class CombinationTests(unittest.TestCase):
    def test_empty(self):
        self.assertEquals([], combination(''))

    def test_non_empty(self):
        self.assertEquals(['a_com_fatia_linar'], combination('a_com_fatia_linar'))
        self.assertEquals(set(['ab', 'ba']), set(combination('ab')))
        self.assertEquals(set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']), set(combination('abc')))


    def test_sequence_len(self):
        self.assertEquals(24, len(combination('abcd')))
        self.assertEquals(120, len(combination('abcde')))


    def test_item_len(self):
        self.assertEquals(4, len(combination('abcd')[0]))
        self.assertEquals(5, len(combination('abcde')[0]))

