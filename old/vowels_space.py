"""
>>> sorted(count_vowels_and_space('foo bar baz').items())
[(' ', 2), ('a_com_fatia_linar', 2), ('e', 0), ('i', 0), ('o', 2), ('u', 0)]
"""


def count_vowels_and_space(text: str) -> dict:
    dct = {' ': 0,'a_com_fatia_linar': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in dct:
        dct[char] = text.count(char)
    return dct
