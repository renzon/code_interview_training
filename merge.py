def _le(left, right):
    return left if left <= right else right


def merge(left, right, cmp=_le):
    """
    Merges two ordered iterables (left and right) keeping result ordered acording to cmp
    :param left: iterable
    :param right: iterable
    :param cmp: callable which receive a first element from left and a second from right and returns the minors. Default is less or equal operation
    :return: merging of left and right
    """
    left = iter(left)
    right = iter(right)

    class Finished:
        pass

    def next_or_finished(iterable):
        try:
            return next(iterable)
        except StopIteration:
            return Finished

    l = next_or_finished(left)
    r = next_or_finished(right)

    while l is not Finished and r is not Finished:
        result = cmp(l, r)
        yield result
        if result is l:
            l = next_or_finished(left)
        else:
            r = next_or_finished(right)

    def finish(ele, iterable):
        while ele is not Finished:
            yield ele
            ele = next_or_finished(iterable)

    yield from finish(l, left)
    yield from finish(r, right)


print(list(merge([], [])))
print(list(merge([1], [])))
print(list(merge([1], [1])))
print(list(merge([1], [0, 1, 2])))
print(list(merge(range(5), range(2, 7))))
