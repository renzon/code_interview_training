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


def read_chars(file):
    yield 1


def test_read_char_is_generator(ascii_file_name):
    assert isinstance(read_chars(ascii_file_name), GeneratorType)
