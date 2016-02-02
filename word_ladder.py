# http://www.programcreek.com/2012/12/leetcode-word-ladder/

def one_diff_char(w, w2): #'dot','hit'
    if len(w)!=len(w2):
        return False
    flag=False
    for c, c2 in zip(w, w2): # flag = True c=o c2=i
        if c!=c2:
            if flag:
                return False
            else:
                flag = True
    return flag



def trans(start, end): # hit, cog
    dct = ["hot","dot","dog","lot","log"]

    def _trans(n, pool):
        for w in pool:
            if one_diff_char(w, end):
                return n
        new_pool=set()
        for w in pool: # w=dot
            for w_dct in dct:
                if one_diff_char(w, w_dct):
                    new_pool.add(w_dct)
        return _trans(n+1,new_pool)

    return _trans(2,set([start]))


# n=3 pool =(dot,lot) new_pool=(hot,dog,lot,dot,log)


import unittest

class Test(unittest.TestCase):
    def test_success(self):
        self.assertEqual(5, trans('hit','cog'))
        self.assertEqual(2, trans('dog','cog'))
        self.assertEqual(3, trans('dot','cog'))

    def test_one_diff_char(self):
        self.assertTrue(one_diff_char('hit','hot'))
        self.assertTrue(one_diff_char('dot','hot'))
        self.assertFalse(one_diff_char('dot','hit'))
        self.assertFalse(one_diff_char('dot','dot'))



