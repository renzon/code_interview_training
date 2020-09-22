# http://www.programcreek.com/2014/06/leetcode-word-ladder-ii-java/

def one_diff_char(w, w2):  # 'dot','hit'
    if len(w) != len(w2):
        return False
    flag = False
    for c, c2 in zip(w, w2):  # flag = True c=o c2=i
        if c != c2:
            if flag:
                return False
            else:
                flag = True
    return flag


def trans(start, end):
    dct = ["hot", "dot", "dog", "lot", "log"]
    visited = set()

    def _trans(pool):
        path_found = False
        for w, path in pool:  # w=log path=(hit,hot, lot,log)
            if one_diff_char(w, end):
                yield path + (end,)
                path_found = True
            if not path_found:
                visited.add(w)
        if path_found:
            return

        new_pool = []
        for w, path in pool:  # w=dot, path = (hit,hot)
            for w_dct in dct:
                if w_dct not in visited and one_diff_char(w, w_dct):
                    w_path = (w_dct, path + (w_dct,))
                    new_pool.append(w_path)
        if len(new_pool) == 0:
            raise Exception('Not existing sequence')
        yield from _trans(new_pool)

    w_path = (start, (start,))
    yield from _trans([w_path])


import unittest


class Test(unittest.TestCase):
    def test_fail(self):
        self.assertRaises(Exception, lambda w, w2: list(trans(w, w2)), 'hit', 'lll')

    def test_success(self):
        self.assertEqual([
            ("hit", "hot", "dot", "dog", "cog"),
            ("hit", "hot", "lot", "log", "cog")],
            list(trans('hit', 'cog')))

    def test_one_diff_char(self):
        self.assertTrue(one_diff_char('hit', 'hot'))
        self.assertTrue(one_diff_char('dot', 'hot'))
        self.assertFalse(one_diff_char('dot', 'hit'))
        self.assertFalse(one_diff_char('dot', 'dot'))
