from unittest.case import TestCase

_buffer = [[0], [1]]


def minor_perfect_squares(n):
    i = 1
    i_square = 1
    while i_square <= n:
        yield i_square
        i += 1
        i_square = i ** 2


def perfec_square_sum(n):
    if n >= len(_buffer):
        for i in range(len(_buffer), n + 1):
            perfect_squares = list(minor_perfect_squares(i))
            if perfect_squares[-1] == i:
                _buffer.append([perfect_squares[-1]])
            else:
                all_combinations = (perfec_square_sum(p) + perfec_square_sum(n - p) for p in perfect_squares)
                minor_len_comb = min(all_combinations, key=len)
                _buffer.append(minor_len_comb)

    return _buffer[n]


class PerfectSquareSumTests(TestCase):
    def test_sucess(self):
        self.assertListEqual([0], perfec_square_sum(0))
        self.assertListEqual([1], perfec_square_sum(1))
        self.assertListEqual([1, 1], perfec_square_sum(2))
        self.assertListEqual([1, 1, 1], perfec_square_sum(3))
        self.assertListEqual([4], perfec_square_sum(4))
        self.assertListEqual([1, 4], perfec_square_sum(5))
        self.assertListEqual([1, 1, 4], perfec_square_sum(6))
        self.assertListEqual([1, 1, 1, 4], perfec_square_sum(7))
        self.assertListEqual([4, 4], perfec_square_sum(8))
        self.assertListEqual([9], perfec_square_sum(9))
        self.assertListEqual([1, 9], perfec_square_sum(10))







