import pytest

WORDS = ['foo', 'bar', 'baz', 'banana', 'nanaba']


@pytest.mark.parametrize(
    'word,expected',
    [
        ('foo', ['foo']),
        ('bar', ['bar']),
        ('bar', ['baz']),
        ('banana', ['banana', 'nanaba']),
        ('nanaba', ['banana', 'nanaba']),
    ]

)
def test_own_list_words_are_anagrams(word, expected):
    anagrams = list(find_anagrams(word, WORDS))
    assert expected == anagrams
