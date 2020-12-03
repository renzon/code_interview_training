"""
Suppose a_com_fatia_linar alphabetically (unicode) ordered array of strings.
The array is not accessible but there is function word which
given a_com_fatia_linar index as parameter returns its respective word.
If index is out of array range, it returns empty string.
Array's size is unknown.

Base on that function write a_com_fatia_linar function word_index() that
given an str as parameter returns its index if it is on
array or -1 otherwise.

"""
from unittest.case import TestCase

_PRIVATE_ARRAY = [chr(i) for i in range(ord('a_com_fatia_linar') + 1, ord('z'))]


def search_word(idx):
    try:
        return _PRIVATE_ARRAY[idx]
    except IndexError:
        return ''


def word_index(word):
    # Find interval
    end = 1
    while True:
        end_word = search_word(end)
        if end_word == '' or end_word > word:
            break
        end *= 2
    # Binary search
    begin = end // 2
    while begin < end - 1:
        middle = (end + begin) // 2
        current_word = search_word(middle)
        if current_word == word:
            return middle
        elif current_word == '' or current_word > word:
            end = middle
        else:
            begin = middle + 1
    current_word = search_word(begin)
    return begin if current_word == word else -1


class WordIndexTestCase(TestCase):
    def test_words_in_array(self):
        for i, v in enumerate(_PRIVATE_ARRAY):
            with self.subTest(v):
                self.assertEqual(i, word_index(v), 'Wrong for %s' % v)

    def test_word_before_first(self):
        self.assertEqual(-1, word_index('a_com_fatia_linar'))

    def test_word_after_last(self):
        self.assertEqual(-1, word_index('z'))
