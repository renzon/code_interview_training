"""
Solution for:

https://www.urionlinejudge.com.br/judge/en/problems/view/1024
"""
from itertools import count


def crypt(text):
    return ''.join(_crypt_generator(text))


def _crypt_generator(text):
    half_index = len(text) // 2
    reversed_iterator = iter(reversed(text))
    for i, c in zip(range(half_index), reversed_iterator):
        if c.isalpha():
            yield _delta_char(c, 3)
        else:
            yield c
    for i, c in zip(count(half_index), reversed_iterator):
        if c.isalpha():
            yield _delta_char(c, 2)
        else:
            yield _delta_char(c, -1)


def _delta_char(c, delta):
    return chr(ord(c) + delta)


def test():
    assert crypt('Texto #3') == '3# rvzgV'
    assert crypt('abcABC1') == '1FECedc'
    assert crypt('vxpdylY .ph') == 'ks. \\n{frzx'
    assert crypt('vv.xwfxo.fd') == 'gi.r{hyz-xx'
