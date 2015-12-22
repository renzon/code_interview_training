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


def perm_breadth_first(seq):
    stack = [(tuple(), tuple(seq)), None]

    while stack:
        result, possibilities = stack.pop()
        if possibilities:
            for p in reversed(possibilities):
                next_result = result + (p,)
                next_possibilities = tuple(filter(lambda e: e != p, possibilities))
                stack.append((next_result, next_possibilities))
        else:
            yield result


def perm_deep_first(seq):
    stack = [(tuple(), tuple(seq), 0)]
    while stack:
        result, possibilities, cursor = stack.pop()
        if cursor == len(possibilities) and len(result) == len(seq):
            yield result
        elif cursor < len(possibilities):
            stack.append((result, possibilities, cursor + 1))
            current_possibility = possibilities[cursor]
            result += (current_possibility,)
            possibilities = tuple(filter(lambda p: p != current_possibility, possibilities))
            stack.append((result, possibilities, 0))


for p in perm_deep_first('ABC'):
    print(p)
