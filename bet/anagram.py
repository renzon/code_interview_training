from collections import Counter
from random import shuffle

import pytest

WORDS = ['foo', 'bar', 'baz', 'banana', 'nanaba']


def find_anagrams(word, target_set):
    """Generate words present on target_set which are an anagram of word

    :param word: str
    :param target_set: iterable with available words
    :return: generator
    """
    word_letters_count = Counter(word)
    for target_word in target_set:
        target_letters_count = Counter(target_word)
        if word_letters_count == target_letters_count:
            yield target_word


SAMPLE = [('foo', ['foo']), ('bar', ['bar']), ('baz', ['baz']), ('banana', ['banana', 'nanaba']),
          ('nanaba', ['banana', 'nanaba']), ]


@pytest.mark.parametrize('word,expected', SAMPLE)
def test_own_list_words_are_anagrams(word, expected):
    anagrams = list(find_anagrams(word, WORDS))
    assert expected == anagrams


@pytest.mark.parametrize('word', ['foo ', 'bananas', '', 'ba', 'bar8'])
def test_negative_anagram_match(word):
    anagrams = list(find_anagrams(word, WORDS))
    assert [] == anagrams


@pytest.mark.parametrize('word,expected', SAMPLE)
def test_shuffled(word, expected):
    shuffled_letters = list(word)
    shuffle(shuffled_letters)
    word = ''.join(shuffled_letters)
    anagrams = list(find_anagrams(word, WORDS))
    assert expected == anagrams
