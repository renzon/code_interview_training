# coding: UTF-8
from __future__ import absolute_import

import string


def counter(s):
    vowel = set('aeiouAEIOU')
    consonants = set(c for c in string.ascii_letters if c not in vowel)

    def count_vowel(c):
        if c in vowel:
            return 1
        return 0

    def count_consonant(c):
        if c in consonants:
            return 1
        return 0

    return sum(map(count_vowel, s)), sum(map(count_consonant, s)),


def test():
    assert (3, 3) == counter('banana')
    assert (10, 11) == counter('Meu pintinho amarelinho')
