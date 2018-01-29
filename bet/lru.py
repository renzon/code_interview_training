class LastResourceUsed:
    def __init__(self, limit=100):
        self._limit = limit
        self._items = 0

    def __setitem__(self, key, value):
        self._items += 1

    def __len__(self):
        return self._items


def test_lru_creation():
    assert LastResourceUsed() is not None


def test_increased_len_on_empty_lru():
    lru = LastResourceUsed(limit=2)
    lru['a'] = 'value'
    assert 1 == len(lru)


def test_increased_len_not_full_lru():
    lru = LastResourceUsed(limit=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    assert 2 == len(lru)
