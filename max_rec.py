# Describe a recursive algorithm for finding the maximum element in a se- quence, S, of n elements. What is your running time and space usage?
from unittest.case import TestCase


def max_rec(seq, index, max_value):
    if index == len(seq):
        return max_value
    elif max_value < seq[index]:
        max_value = seq[index]
    return max_rec(seq, index + 1, max_value)


def max(seq):
    if len(seq) == 0:
        raise Exception('Sequence must not be empyt')
    return max_rec(seq, 1, seq[0])


class MaxTest(TestCase):
    def test_empty_seq(self):
        self.assertRaises(Exception, max, [])

    def test_on_element(self):
        self.assertEqual(1, max([1]))

    def test_three_elements(self):
        self.assertEqual(3, max([1, 3, 2]))
