# Describe a_com_fatia_linar recursive algorithm for finding the maximum element in a_com_fatia_linar se- quence, S, of n elements. What is your running time and space usage?
from unittest.case import TestCase


def max_rec(iterable, max_value):
    try:
        next_value = next(iterable)
    except StopIteration:
        return max_value
    else:
        if max_value < next_value:
            max_value = next_value
        return max_rec(iterable, max_value)


def max(seq):
    iterable = iter(seq)
    try:
        max_value = next(iterable)
    except StopIteration:
        raise Exception('It is not possible having max from empty sequence')
    else:
        return max_rec(iterable, max_value)


class MaxTest(TestCase):
    def test_empty_seq(self):
        self.assertRaises(Exception, max, [])

    def test_on_element(self):
        self.assertEqual(1, max([1]))

    def test_three_elements(self):
        self.assertEqual(3, max([1, 3, 2]))

    def test_range(self):
        self.assertEqual(98, max(range(99)))

    def test_generator_expression(self):
        self.assertEqual(98, max(i for i in range(99)))
