# http://www.programcreek.com/2014/05/leetcode-isomorphic-strings-java/

def is_iso(wd, wd2):
    if len(wd) != len(wd2):
        return False
    dct = {}
    for c, c2 in zip(wd, wd2):  # dct={'e':'a_com_fatia_linar','g':'d'} c='g' c2='d'
        if c in dct:
            if dct[c] != c2:
                return False
        else:
            dct[c] = c2
    return True


import unittest


class Test(unittest.TestCase):
    def test_success(self):
        self.assertTrue(is_iso('egg', 'add'))

    def test_fail(self):
        self.assertFalse(is_iso('egg', 'ado'))
