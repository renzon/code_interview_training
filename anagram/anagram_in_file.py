import os
import string
from collections import deque, Counter
from itertools import islice
from types import GeneratorType

import pytest

def test_fail():
    pytest.fail('Foo')


def generate_file(file_name, content):
    with open(file_name, 'w', encoding='utf8') as file:
        for char in content:
            file.write(char)
    return file_name


@pytest.fixture(scope='session')
def ascii_file_name():
    file_name = 'ascii.txt'
    yield generate_file(file_name, string.ascii_letters)
    os.remove(file_name)


PT_BR_SPECIAL_LETTERS = 'çãõáàú'


@pytest.fixture(scope='session')
def ptbr_file_name():
    file_name = 'pt_br.txt'
    yield generate_file(file_name, PT_BR_SPECIAL_LETTERS)
    os.remove(file_name)


@pytest.fixture(scope='session')
def banana_file_name():
    file_name = 'pt_br.txt'
    yield generate_file(file_name, 'banana')
    os.remove(file_name)


def read_chars(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        while True:
            char = file.read(1)
            if len(char) == 1:
                yield char
            else:
                break


def test_read_char_is_generator(ascii_file_name):
    assert isinstance(read_chars(ascii_file_name), GeneratorType)


def test_read_ascii_chars(ascii_file_name):
    assert string.ascii_letters == ''.join(read_chars(ascii_file_name))


def test_read_ptbr_chars(ptbr_file_name):
    assert PT_BR_SPECIAL_LETTERS == ''.join(read_chars(ptbr_file_name))


def anagrams_in_file(file_name, pattern):
    found = set()
    pattern_char_freq = Counter(pattern)
    chars_generator = read_chars(file_name)
    n = len(pattern)
    buffer = deque(islice(chars_generator, n), maxlen=n)
    buffer_char_freq = Counter(buffer)

    if pattern_char_freq == buffer_char_freq:
        s = ''.join(buffer_char_freq)
        yield s
        found.add(s)

    for char in chars_generator:
        pop_char = buffer[0]
        buffer_char_freq[pop_char] -= 1
        if buffer_char_freq[pop_char] == 0:
            del buffer_char_freq[pop_char]
        buffer.append(char)
        buffer_char_freq[char] += 1
        if pattern_char_freq == buffer_char_freq:
            s = ''.join(buffer_char_freq)
            if s not in found:
                yield s
                found.add(s)


def test_anagrams_in_file_is_generator(ascii_file_name):
    assert isinstance(anagrams_in_file(ascii_file_name, 'foo'), GeneratorType)


@pytest.mark.parametrize(
    'char',
    list(string.ascii_letters)
)
def test_anagrams_ascii_char(char, ascii_file_name):
    assert [char] == list(anagrams_in_file(ascii_file_name, char))


@pytest.mark.parametrize(
    'pattern',
    'na an'.split()
)
def test_anagrams_na(pattern, banana_file_name):
    assert ['an', 'na'] == list(anagrams_in_file(banana_file_name, pattern))
