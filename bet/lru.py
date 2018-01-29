from collections import OrderedDict


class LastResourceUsed:
    def __init__(self, limit=100):
        self._limit = limit
        self._items = OrderedDict()

    def __setitem__(self, key, value):
        if len(self) < self._limit:
            self._items[key] = value

    def __len__(self):
        return len(self._items)

    def __getitem__(self, key):
        return self._items[key]


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


def test_constant_len_on_full_lru():
    lru = LastResourceUsed(limit=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    lru['c'] = 'value c'
    assert 2 == len(lru)


def test_item_retrieval():
    lru = LastResourceUsed(limit=2)
    lru['a'] = 'value a'
    assert 'value a' == lru['a']
