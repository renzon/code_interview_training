from itertools import permutations

items = [1, 2, 3, 4]
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

    class State():
        def __init__(self, remaining_items, permutation, r):
            self.r = r
            self.permutation = permutation
            self.remaining_items = remaining_items

        def next_state_without_first_remaining_element(self):
            return State(self.remaining_items[1:], self.permutation, self.r)

        def next_state_with_element(self, element_index):
            new_remaining = self.remaining_items[:element_index] + self.remaining_items[element_index + 1:]
            new_permutation = list(self.permutation)
            new_permutation.append(self.remaining_items[element_index])
            return State(new_remaining, new_permutation, self.r - 1)


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
                state_stack.append(current_state.next_state_without_first_remaining_element())
                for remaining_idx, _ in enumerate(current_state.remaining_items):
                    state_stack.append(current_state.next_state_with_element(remaining_idx))


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


def all_permutations(items):
    if not items:
        yield items

    class State():
        def __init__(self, remaining_items, permutation):
            self.permutation = permutation
            self.remaining_items = remaining_items

        def next_state_without_first_remaining_element(self):
            return State(self.remaining_items[1:], self.permutation)

        def next_state_with_element(self, element_index):
            new_remaining = self.remaining_items[:element_index] + self.remaining_items[element_index + 1:]
            new_permutation = list(self.permutation)
            new_permutation.append(self.remaining_items[element_index])
            return State(new_remaining, new_permutation)
        def __repr__(self):
            return 'State(%r, %r)' % (self.remaining_items, self.permutation)


    state_stack = []

    for idx, value in enumerate(items):
        permutation = [value]
        remaining_items = items[:idx] + items[idx + 1:]
        state_stack.append(State(remaining_items, permutation))
        while state_stack:
            current_state = state_stack.pop()
            if current_state.remaining_items:
                for remaining_idx in reversed(range(0,len(current_state.remaining_items))):
                    state_stack.append(current_state.next_state_with_element(remaining_idx))
            yield current_state.permutation


print(list(all_permutations(items)))
