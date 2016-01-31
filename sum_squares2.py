from functools import lru_cache
from itertools import takewhile


def sq_le(n):
    genexp = (i ** 2 for i in range(1, n + 1))
    return takewhile(lambda sq: sq <= n, genexp)


@lru_cache(maxsize=1024)
def min_sum_squares(n):
    if n == 0:
        return [0]

    def rec(remaining):  # remaining= 1
        if remaining == 0:
            return []
        else:
            min_solution = None
            for sq in sq_le(remaining):
                new_remaining = remaining - sq
                sol = rec(new_remaining)
                if min_solution is None or len(min_solution) > (len(sol) + 1):
                    min_solution = sol + [sq]
            return min_solution

    return rec(n)


def generate_sum_sq_func():
    cache = [[], [1]]

    def min_sum(n):
        if n == 0:
            return [0]
        while len(cache) < n + 1:
            i = len(cache)
            items = ((cache[i - sq], sq) for sq in sq_le(i))
            min_previous_solution, respective_square = min(items, key=lambda tpl: len(tpl[0]))
            cache.append(min_previous_solution + [respective_square])
        return cache[n]

    return min_sum


min_sum = generate_sum_sq_func()

for i in range(13):
    print(i, min_sum(i))
