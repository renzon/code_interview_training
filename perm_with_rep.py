import pytest


def perm_with_rep(seq):
    pass


@pytest.mark.parametrize(
    'seq,expected',
    [
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
