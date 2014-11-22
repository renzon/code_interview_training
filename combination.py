from collections import namedtuple
from itertools import combinations

items = [1, 2, 3, 4]
comb_number = 2
print(list(combinations(items, comb_number)))


def comb(items, n):
    if n > len(items):
        return []

    def comb_rec(combination, begin):
        if len(combination) == n:
            yield combination
        elif len(combination) < n:
            for idx in range(begin, len(items)):
                possible_comb = list(combination) + [items[idx]]
                yield from comb_rec(possible_comb, idx + 1)


    for idx, value in enumerate(items):
        combination = [value]
        yield from comb_rec(combination, idx + 1)


print(list(comb(items, comb_number)))


def comb(item, n):
    if n <= 0 or len(item) < n:
        return []
    comb_stack = []
    State = namedtuple('State', ('idx', 'comb'))
    for idx, value in enumerate(items):
        comb_stack.append(State(idx + 1, [value]))
        while comb_stack:
            current_state = comb_stack.pop()
            current_index = current_state.idx
            current_comb = current_state.comb
            if len(current_comb) == n:
                yield current_comb
            elif current_index < len(item) and len(current_comb) < n:
                comb_stack.append(State(current_index + 1, current_comb))
                comb_stack.append(State(current_index + 1, list(current_comb) + [item[current_index]]))


print(list(comb(items, comb_number)))


def all_combinations(items):
    if not items:
        return items

    def recursive_combination(begin, combination):
        if begin <= len(items):
            yield list(combination)
            for idx in range(begin, len(items)):
                next_combination = list(combination)
                next_combination.append(items[idx])
                yield from recursive_combination(idx + 1, next_combination)


    for idx, value in enumerate(items):
        combination = [value]
        yield from recursive_combination(idx + 1, combination)


print(list(all_combinations(items)))