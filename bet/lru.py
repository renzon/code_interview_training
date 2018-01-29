from collections import OrderedDict
from unittest.mock import Mock


class LRUMiss(Exception):
    pass


import pytest


class LastResourceUsed:
    """Class implementing LRU using OrderedDict as base.
    Know isssue: age update is O(n)
    """

    def __init__(self, limit=100):
        self._limit = limit
        self._items = OrderedDict()

    def __setitem__(self, key, value):
        if len(self) == self._limit:
            self._items.popitem(last=False)
        self._items[key] = value

    def __len__(self):
        return len(self._items)

    def __getitem__(self, key):
        try:
            value = self._items[key]
        except KeyError:
            raise LRUMiss(f'Item {key} no present on LRU') from KeyError
        else:
            # Updating age before returning value
            self._items.pop(key)
            self._items[key] = value
            return value


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


def test_lru_miss():
    lru = LastResourceUsed(limit=2)
    with pytest.raises(LRUMiss):
        lru['a']


def test_oldest_used_item_removed():
    lru = LastResourceUsed(limit=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    lru['c'] = 'value c'
    with pytest.raises(LRUMiss):
        lru['a']


def test_oldest_used_item_updated():
    lru = LastResourceUsed(limit=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    _ = lru['a']  # to update a use
    lru['c'] = 'value c'
    with pytest.raises(LRUMiss):
        lru['b']


def lru(func):
    func._cache = LastResourceUsed()
    return func


def test_lru_decorator_cach_attribute():
    mock = Mock()

    @lru
    def f(*args, **kwargs):
        return mock(*args, **kwargs)

    assert isinstance(f._cache, LastResourceUsed)
