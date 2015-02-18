def combination(sequence, size=None):
    if size is None:
        size = len(sequence)

    def _recursive_combination(current_sequence, current_combination, free_positions):
        if free_positions > len(current_sequence):
            return

        if free_positions == 0 and len(current_combination) == size and current_combination:
            yield current_combination
        elif free_positions > 0:
            # combinations not including last element
            next_sequence = current_sequence[:-1]
            yield from _recursive_combination(next_sequence, current_combination, free_positions)

            # combinations including last element
            current_combination += current_sequence[-1]
            yield from _recursive_combination(next_sequence, current_combination, free_positions - 1)

    yield from _recursive_combination(sequence, '', size)


import unittest


class CombinationTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], list(combination('')))

    def test_longer_combinations(self):
        self.assertEqual([], list(combination('a', 2)))

    def test_combinations(self):
        self.assertEqual([], list(combination('abc', 0)))
        self.assertEqual(set(['a', 'b', 'c']), set(combination('abc', 1)))
        self.assertEqual(set(['ba', 'ca','cb']), set(combination('abc', 2)))
        self.assertEqual(['cba'], list(combination('abc', 3)))
		
	
