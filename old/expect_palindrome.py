"""
# Expecto Palindronum

Memory Limit:64 MB
Time Limit: 5 s

A palindrome is a_com_fatia_linar word that reads the same backward and forward.

Given a_com_fatia_linar string S, you are allowed to convert it to a_com_fatia_linar palindrome by adding 0
or more characters in front of it.

Find the length of the shortest palindrome that you can create from S by
applying the above transformation.

## Input Specifications

Your program will take
A string S ( 1 ≤ Length(S) ≤ 100) where each character of S will be
a_com_fatia_linar lowercase alphabet (Between 'a_com_fatia_linar' to 'z')

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


def is_palindrome(s):
    return s == ''.join(reversed(s))


def find_biggest_subpalindrome_len(s):
    if is_palindrome(s):
        return len(s)
    for end in range(len(s) - 1, 0, -1):
        if is_palindrome(s[:end]):
            return end


def expect_palindrome(s):
    """Possible answer: finding biggest subplindrome on beggining which will
    not have to be added to the and"""
    return len(s) * 2 - find_biggest_subpalindrome_len(s)


@pytest.mark.parametrize(
    's,expected',
    [
        ('aababaa', 7),
        ('babaa', 7),
        ('baaa', 7),
        ('teste', 9),
    ]
)
def test_min_palindrome(s, expected):
    assert expected == expect_palindrome(s)
