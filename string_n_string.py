from itertools import chain


def string_n_string(s, n):
    chars = list(s)
    s_len = len(s)
    odd_index_start = (s_len + 1) // 2
    for _ in range(n):
        even = (char for i, char in enumerate(s) if i % 2 == 0)
        odd = (char for i, char in enumerate(s) if i % 2 != 0)
        s = ''.join(chain(even, odd))

    return s


def test():
    assert string_n_string("Wow Example!", 1) == "WwEapeo xml!"
    assert string_n_string("qwertyuio", 2) == "qtorieuwy"
