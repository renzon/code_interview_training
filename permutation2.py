def _perm_rec(previous_result, possibilities):
    if possibilities:
        for p in possibilities:
            next_result = previous_result + (p,)
            next_possibilities = tuple(filter(lambda e: e != p, possibilities))
            yield from _perm_rec(next_result, next_possibilities)
    else:
        yield previous_result


def perm(seq):
    previous_result = tuple()
    possibilities = tuple(seq)
    yield from _perm_rec(previous_result, possibilities)


def perm_non_rec(seq):
    stack = [(tuple(), tuple(seq))]

    while stack:
        result, possibilities = stack.pop()
        if possibilities:
            for p in reversed(possibilities):
                next_result = result + (p,)
                next_possibilities = tuple(filter(lambda e: e != p, possibilities))
                stack.append((next_result, next_possibilities))
        else:
            yield result


for p in perm_non_rec('ABC'):
    print(''.join(p))
