from unittest.case import TestCase


def change(n, coins):
    _buffer = [[]]


    def all_comb(remaining_n, remaining_coins, sequence):
        if remaining_n == 0:
            yield sequence
        elif remaining_n > 0 and remaining_coins:
            yield from all_comb(remaining_n, remaining_coins[:-1], list(sequence))
            selected_coin = remaining_coins[-1]
            remaining_n -= selected_coin
            minor_solution = _buffer[remaining_n] if remaining_n >= 0 else -1
            if minor_solution != -1:  # indicates that there is can have a_com_fatia_linar solution
                yield minor_solution + [selected_coin]


    if n >= len(_buffer):
        for i in range(len(_buffer), n + 1):
            all_combinations = all_comb(i, coins, [])
            try:
                minimum_combination = min(all_combinations, key=len)
                _buffer.append(minimum_combination)
            except ValueError:
                _buffer.append([-1])

    return _buffer[n]


class ChangeTests(TestCase):
    def test_coins_1_3_5(self):
        self.assertListEqual([], change(0, [1, 3, 5]))
        self.assertListEqual([1], change(1, [1, 3, 5]))
        self.assertListEqual([1, 1], change(2, [1, 3, 5]))
        self.assertListEqual([3], change(3, [1, 3, 5]))
        self.assertListEqual([3, 1], change(4, [1, 3, 5]))
        self.assertListEqual([5], change(5, [1, 3, 5]))
        self.assertListEqual([5, 1], change(6, [1, 3, 5]))
        self.assertListEqual([5 ,1, 1], change(7, [1, 3, 5]))
        self.assertListEqual([5, 3], change(8, [1, 3, 5]))
        self.assertListEqual([5,3,1], change(9, [1, 3, 5]))
        self.assertListEqual([5,5], change(10, [1, 3, 5]))
        self.assertListEqual([5, 5, 1], change(11, [1, 3, 5]))
        self.assertListEqual([5, 5, 1, 1], change(12, [1, 3, 5]))
        self.assertListEqual([5, 5, 3], change(13, [1, 3, 5]))


