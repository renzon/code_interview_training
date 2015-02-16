# Number notation

def encode(n):
    if n == 0:
        return ''
    dct = {'': 0}
    while True:
        new_items = {}
        for k, v in dct.items():
            factor = 2 ** len(k)
            if len(k) % 2 == 0:
                factor *= -1
            new_k = k + '1'
            new_v = factor + v
            if new_v == n:
                return new_k
            new_items[new_k] = new_v
            new_items[k + '0'] = v
        dct.update(new_items)


import unittest


class RepresentationTests(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual('', encode(0))
        self.assertEqual('1', encode(-1))
        self.assertEqual('01', encode(2))
        self.assertEqual('11', encode(1))
        self.assertEqual('001', encode(-4))
        self.assertEqual('101', encode(-5))
        self.assertEqual('011', encode(-2))
        self.assertEqual('111', encode(-3))

