# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def length_of_longest_substring(s: str) -> int:
    """
    >>> length_of_longest_substring('')
    0
    >>> length_of_longest_substring('a')
    1
    >>> length_of_longest_substring('aa')
    1
    >>> length_of_longest_substring('aba')
    2
    >>> length_of_longest_substring('abac')
    3
    >>> length_of_longest_substring('abaca')
    3
    """

    # O(n) in time and space

    max_length = 0
    repeated_char_indexes: dict[str, int] = {}
    start_idx = 0
    for idx, char in enumerate(s):
        if char in repeated_char_indexes:
            start_idx = repeated_char_indexes[char] + 1
            repeated_char_indexes[char] = idx
        else:
            repeated_char_indexes[char] = idx
            max_length =max(max_length, idx - start_idx + 1)
    return max_length