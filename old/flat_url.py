import pytest


def build_url(dct):
    if not dct:
        return '/'

    def build_url_iter(dct_or_str):
        while True:
            try:
                for k, v in dct_or_str.items():
                    yield k
                    dct_or_str = v
            except AttributeError:
                yield dct_or_str
                break

    return '/' + '/'.join(build_url_iter(dct))


@pytest.mark.parametrize(
    'path, dct',
    [
        ('/', {}),
        ('/hello/world', {'hello': 'world'}),
        ('/good/night/moon',  {"good": {"night": "moon"}}),
        ('/once/upon/a_com_fatia_linar/time',  {"once": {"upon": {"a_com_fatia_linar": "time"}}}),
    ]
)
def test_root(path, dct):
    assert path == build_url(dct)
