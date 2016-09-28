"""
Suppose a alphabetically (unicode) ordered array of strings.
The array is not accessible but there is function word which
given a index as parameter returns its respective word.
If index is out of array range, it returns empty string.
Array's size is unknown.

Base on that function write a function word_index() that
given an str as parameter returns its index if it is on
array or -1 otherwise.

"""
from unittest.case import TestCase

_PRIVATE_ARRAY = [str(i) for i in range(ord('a') + 1, ord('z'))]


def word(idx):
    try:
        return _PRIVATE_ARRAY[idx]
    except IndexError:
        return ''


def word_index(word):
    pass


class WordIndexTestCase(TestCase):
    def test_words_in_array(self):
        for i, v in _PRIVATE_ARRAY:
            with self.subTest(v):
                self.assertEqual(i, word_index(v))

    def test_word_before_first(self):
        self.assertEqual(-1, word_index('a'))

    def test_word_after_last(self):
        self.assertEqual(-1, word_index('z'))
