from collections import OrderedDict
from functools import partial, wraps
from unittest.mock import Mock


class LRUMiss(Exception):
    pass


import pytest


class LastResourceUsed:
    """Class implementing LRU using OrderedDict as base.
    Know isssue: age update is O(n)
    """

    def __init__(self, max_size=100):
        self._max_size = max_size
        self._items = OrderedDict()

    def __setitem__(self, key, value):
        if len(self) == self._max_size:
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


def lru(func=None, *, max_size=100):
    if func is None:
        return partial(lru, max_size=max_size)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper._cache = LastResourceUsed(max_size=max_size)
    return wrapper


def test_lru_creation():
    assert LastResourceUsed() is not None


def test_increased_len_on_empty_lru():
    lru = LastResourceUsed(max_size=2)
    lru['a'] = 'value'
    assert 1 == len(lru)


def test_increased_len_not_full_lru():
    lru = LastResourceUsed(max_size=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    assert 2 == len(lru)


def test_constant_len_on_full_lru():
    lru = LastResourceUsed(max_size=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    lru['c'] = 'value c'
    assert 2 == len(lru)


def test_item_retrieval():
    lru = LastResourceUsed(max_size=2)
    lru['a'] = 'value a'
    assert 'value a' == lru['a']


def test_lru_miss():
    lru = LastResourceUsed(max_size=2)
    with pytest.raises(LRUMiss):
        lru['a']


def test_oldest_used_item_removed():
    lru = LastResourceUsed(max_size=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    lru['c'] = 'value c'
    with pytest.raises(LRUMiss):
        lru['a']


def test_oldest_used_item_updated():
    lru = LastResourceUsed(max_size=2)
    lru['a'] = 'value a'
    lru['b'] = 'value b'
    _ = lru['a']  # to update a use
    lru['c'] = 'value c'
    with pytest.raises(LRUMiss):
        lru['b']


def test_lru_decorator_cach_attribute():
    @lru
    def f():
        pass

    assert isinstance(f._cache, LastResourceUsed)


def test_lru_decorator_default_max_size():
    @lru
    def f():
        pass

    assert 100 == f._cache._max_size


def test_lru_decorator_non_default_max_size():
    @lru(max_size=10)
    def f():
        pass

    assert 10 == f._cache._max_size


def test_lru_call_not_on_cache():
    mock = Mock()
    decorated = lru(max_size=2)(mock)
    decorated(1, 2)
    mock.assert_called_once_with(1, 2)
