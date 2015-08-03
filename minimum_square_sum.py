_square_sums = [[0], [1]]


def calculate_lesser_squares(n):
    for i in range(1, n + 1):
        i **= 2
        if i <= n:
            yield i


def generate_all_possibilities(lesser_squares, n):
    for l_square in lesser_squares:
        yield [l_square] + _square_sums[n - l_square]


def minimum_square_sum(n):
    """
    Return the min list of square number which sum is n

    :param n: a integer to search
    :return: the min list
    """

    if n >= len(_square_sums):
        for i in range(len(_square_sums), n+1):
            lesser_squares = list(calculate_lesser_squares(i))
            if lesser_squares[-1] == i:
                _square_sums.append([i])
            else:
                all_possibilities = generate_all_possibilities(lesser_squares, i)
                _square_sums.append(min(all_possibilities, key=len))
    return _square_sums[n]


from unittest.case import TestCase


class Tests(TestCase):
    def test_0(self):
        self.assertListEqual([0], minimum_square_sum(0))

    def test_1(self):
        self.assertListEqual([1], minimum_square_sum(1))

    def test_2(self):
        self.assertListEqual([1, 1], minimum_square_sum(2))

    def test_3(self):
        self.assertListEqual([1, 1, 1], minimum_square_sum(3))

    def test_4(self):
        self.assertListEqual([4], minimum_square_sum(4))

    def test_12(self):
        self.assertListEqual([4, 4, 4], minimum_square_sum(12))
