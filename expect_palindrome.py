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


def expect_palindrome(s):
    return len(s) * 2 - 1


@pytest.mark.parametrize(
    's,expected',
    [
        ('babaa', 7),
        ('baaa', 7),
        ('teste', 9),
    ]
)
def test_min_palindrome(s, expected):
    assert expected == expect_palindrome(s)
