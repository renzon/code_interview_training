from collections import Counter, OrderedDict

import pytest


def perm_with_rep(seq):
    frequencies = Counter(seq)
    stack = []
    stack.append(('', frequencies))
    while stack:
        prefix, frequencies = stack.pop()
        if len(frequencies) == 0:
            yield prefix
            continue

        for char, frequency in frequencies.items():
            next_prefix = prefix + char
            next_frequencies = dict(frequencies)
            if frequency == 1:
                del next_frequencies[char]
            else:
                next_frequencies[char] -= 1
            stack.append((next_prefix, next_frequencies))


def _perm_with_rep(current_s, chars_frequency):
    if len(chars_frequency) == 0:
        yield current_s
    for char, freq in chars_frequency.items():
        next_s = current_s + char
        if freq == 1:
            next_chars_frequency = dict(chars_frequency)
            del next_chars_frequency[char]
        else:
            next_chars_frequency = chars_frequency
        chars_frequency[char] -= 1
        yield from _perm_with_rep(next_s, next_chars_frequency)
        chars_frequency[char] += 1


def perm_with_rep(seq):
    chars_frequency = OrderedDict(Counter(seq).items())
    yield from _perm_with_rep('', chars_frequency)


@pytest.mark.parametrize(
    'seq,expected',
    [
        ('', {''}),
        ('1', {'1'}),
        ('12', set('12 21'.split())),
        ('123', set('123 312 231 321 132 213'.split())),
    ]
)
def test_all_different(seq, expected):
    assert expected == set(perm_with_rep(seq))


@pytest.mark.parametrize(
    'seq,expected',
    [
        ('11', {'11'}),
        ('112', set('112 121 211'.split())),
        ('1122', set('1122 2112 2211 1221 1212 2121'.split())),
    ]
)
def test_repeated(seq, expected):
    assert expected == set(perm_with_rep(seq))
