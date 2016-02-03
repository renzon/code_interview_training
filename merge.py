def _le(left, right):
    return left if left <= right else right


def merge(left, right, cmp=_le):
    """
    Merges two ordered iterables (left and right) keeping result ordered according to cmp.

    :param left: iterable
    :param right: iterable
    :param cmp: callable which receive one element from left and another from right and returns the on to be merged.
    Default is less or equal then. Ex:
    def _le(left, right):
        return left if left <= right else right
    :return: merging result of left and right

    Usage:

    >>> from merge import merge
    >>> print(list(merge([1, 2], [3, 4])))
    [1, 2, 3, 4]
    >>> print(list(merge([1, 2], [0, 4])))
    [0, 1, 2, 4]
    >>> print(list(merge(range(3), range(2,5))))
    [0, 1, 2, 2, 3, 4]
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
