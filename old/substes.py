from unittest.case import TestCase


def _subset_rec(sets, iterable):
    try:
        element = next(iterable)
    except StopIteration:
        return sets
    else:
        subsets_with_element = [subset + [element] for subset in sets]
        sets.extend(subsets_with_element)
        return _subset_rec(sets, iterable)


def subsets(iterable):
    sets = [[]]
    iterable = iter(iterable)
    return _subset_rec(sets, iterable)


class SubsetsTests(TestCase):
    def test_empty_set(self):
        self.assertEqual([[]], subsets(''))

    def test_one_element_set(self):
        self.assertListEqual([[], ['A']], subsets('A'))

    def test_two_element_set(self):
        self.assertListEqual([[], ['A'], ['B'], ['A', 'B']], subsets('AB'))

    def test_three_element_set(self):
        self.assertListEqual([[], ['A'], ['B'], ['A', 'B'], ['C'], ['A', 'C'], ['B', 'C'], ['A', 'B', 'C']],
                             subsets('ABC'))
