"""
# Expecto Palindronum

Memory Limit:64 MB
Time Limit: 5 s

A palindrome is a word that reads the same backward and forward.

Given a string S, you are allowed to convert it to a palindrome by adding 0
or more characters in front of it.

Find the length of the shortest palindrome that you can create from S by
applying the above transformation.

## Input Specifications

Your program will take
A string S ( 1 ≤ Length(S) ≤ 100) where each character of S will be
a lowercase alphabet (Between 'a' to 'z')

## Output Specifications

For each input, print out an integer L denoting the length of the shortest
palindrome you can
generate from S.

## Sample Input/Output

INPUT
baaa
OUTPUT
7
EXPLANATION
The shortest palindrome you can construct from 'baaa' is 'aaabaaa'.
"""

import pytest


class PalindromeFound(Exception):
    def __init__(self, search):
        self.search = search


class PalindromeSearch:
    def __init__(self, s, end):
        self.s = s
        self.end = end
        self.cursor_end = end - 1
        self.cursor_begin = 0

    def match(self):
        """ Check if char in cursor_end match cursor_begin.
        If a match occurs cursors are updated.
        :return: boolean
        """
        if self.cursor_begin >= self.cursor_end:
            return True
        result = self.s[self.cursor_begin] == self.s[self.cursor_end]
        if result:
            self.cursor_end -= 1
            self.cursor_begin += 1
        return result

    def __len__(self):
        return self.end


def find_biggest_subpalindrome_len(s):
    """Inspired by https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm"""
    searches = []
    for end in range(len(s), -1, -1):
        searches.append(PalindromeSearch(s, end))
        try:
            searches = [search for search in searches if search.match()]
        except PalindromeFound as found:
            return len(found.search)

    max_search = searches[0]
    return len(max_search)


def expect_palindrome(s):
    """Possible answer: finding biggest subplindrome on beggining which will
    not have to be added to the and"""
    return len(s) * 2 - find_biggest_subpalindrome_len(s)


@pytest.mark.parametrize(
    's,expected',
    [
        ('', 0),
        ('aababaa', 7),
        ('babaa', 7),
        ('baaa', 7),
        ('teste', 9),
    ]
)
def test_min_palindrome(s, expected):
    assert expected == expect_palindrome(s)
