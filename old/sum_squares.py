# Given n, write the short sequence a,b,c..k where all numbers in are perfect squares and its sum is n
from unittest.case import TestCase

cache = [(0,), (1,)]


def calc_minor_sorted_squares(n):
    for i in range(1, n):
        square = i ** 2
        if square <= n:
            yield square
        else:
            break


def sum_square(n):
    while n > (len(cache) - 1):
        next_cache_number = len(cache)
        sorted_squares = list(calc_minor_sorted_squares(next_cache_number))
        if sorted_squares[-1] == next_cache_number:
            cache.append((next_cache_number,))
        else:
            selected_square = None
            min_solution = None
            min_solution_len = next_cache_number
            for square in sorted_squares:
                remain = next_cache_number - square
                remain_solution = sum_square(remain)
                if len(remain_solution) < min_solution_len:
                    min_solution_len = len(remain_solution)
                    min_solution = remain_solution
                    selected_square = square
            cache.append(min_solution + (selected_square,))

    return cache[n]


class SumSquaresTests(TestCase):
    def test_initial_cache(self):
        self.assertTupleEqual((0,), sum_square(0))
        self.assertTupleEqual((1,), sum_square(1))

    def test_first_not_perfect_square(self):
        self.assertTupleEqual((1, 1), sum_square(2))

    def test_first_perfect_square_not_in_cache(self):
        self.assertTupleEqual((4,), sum_square(4))

    def test_trigger_for_greed_solution(self):
        """
        Greed solution try get nearest minor square from n. 9 in case of 12.
        So the solution would include the elements (9,1,1,1) which is not the shortest solution
        """
        self.assertTupleEqual((4, 4, 4), sum_square(12))
