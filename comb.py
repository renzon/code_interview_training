# based on combination from python code

def combination(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    # main ideia is keeping tracking of indices
    indices = list(range(r))

    def comb():
        return tuple(pool[i] for i in indices)

    yield comb()

    while True:
        # looking for a index which can be incremented
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return  # no one index can be incremented any more

        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield comb()


print(list(combination('ABCD', 2)))
print(list(combination('ABCD', 3)))
