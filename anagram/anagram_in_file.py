import string
from types import GeneratorType

import pytest


@pytest.fixture(scope='session')
def ascii_file_name():
    file_name = 'ascii.txt'
    with open(file_name, 'w', encoding='utf8') as file:
        for char in string.ascii_letters:
            file.write(char)

    return file_name


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
