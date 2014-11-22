from collections import deque, namedtuple
from itertools import permutations

items = [1, 2, 3]
n = 2

print(list(permutations(items, n)))


def permutations(items, r=None):
    r = r or len(items)
    if r > len(items) or r == 0:
        yield items

    def recursive_permutations(remaining_items, permutation, r):
        if r == 0:
            yield permutation
        elif r > 0:
            for idx, value in enumerate(remaining_items):
                next_permutation = list(permutation)
                next_permutation.append(value)
                next_remaining_items = remaining_items[:idx] + remaining_items[idx + 1:]
                yield from recursive_permutations(next_remaining_items, next_permutation, r - 1)

    for idx, value in enumerate(items):
        permutation = [value]
        remaining_items = items[:idx] + items[idx + 1:]
        yield from recursive_permutations(remaining_items, permutation, r - 1)


print(list(permutations(items, n)))


def permutations(items, r=None):
    r = r or len(items)
    if r > len(items) or r == 0:
        yield items

    State = namedtuple('State', ('remaining_items', 'permutation', 'r'))

    state_stack = []

    for idx, value in enumerate(items):
        permutation = [value]
        remaining_items = items[:idx] + items[idx + 1:]
        state_stack.append(State(remaining_items, permutation, r - 1))
        while state_stack:
            current_state = state_stack.pop()
            if current_state.r == 0:
                yield current_state.permutation
            elif current_state.r > 0 and current_state.remaining_items:
                next_remaining = current_state.remaining_items[1:]
                next_permutation = list(current_state.permutation)
                next_r = current_state.r
                state_stack.append(State(next_remaining, next_permutation, next_r))
                next_permutation = current_state.permutation
                next_permutation.append(current_state.remaining_items[0])
                next_remaining = current_state.remaining_items[1:]
                next_r = current_state.r-1
                state_stack.append(State(next_remaining, next_permutation, next_r))


print(list(permutations(items, n)))


def all_permutations(items):
    if not items:
        yield items

    def recursive_permutations(remaining_items, permutation):
        yield permutation
        if remaining_items:
            for idx, value in enumerate(remaining_items):
                next_permutation = list(permutation)
                next_permutation.append(value)
                next_remaining_items = remaining_items[:idx] + remaining_items[idx + 1:]
                yield from recursive_permutations(next_remaining_items, next_permutation)

    for idx, value in enumerate(items):
        permutation = [value]
        remaining_items = items[:idx] + items[idx + 1:]
        yield from recursive_permutations(remaining_items, permutation)


print(list(all_permutations(items)))
