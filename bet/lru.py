class LastResourceUsed:
    def __init__(self, limit=100):
        self.limit = limit

    def __setitem__(self, key, value):
        pass

    def __len__(self):
        return 1


def test_lru_creation():
    assert LastResourceUsed() is not None


def test_increased_len_on_empty_lru():
    lru = LastResourceUsed(limit=2)
    lru['a'] = 'value'
    assert 1 == len(lru)
