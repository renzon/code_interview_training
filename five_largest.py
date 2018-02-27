"""
Allow non negative numbers be appended to a data structure and provide 5 largest appended numbers.

Requisites:

1) No sort or index method can be used
2) No more than 6 numbers can be kept on memory

"""


class NegativaNumberAdded(Exception):
    pass


class FiveLargest:
    """
    Calculate the five largest numbers appended. Only non integers number can be accepted.

    Ex:

    >>> five_largest=FiveLargest()
    >>> list(five_largest.largest_numbers())
    []
    >>> five_largest.append(0)
    >>> list(five_largest.largest_numbers())
    [0]
    >>> five_largest.append(1)
    >>> sorted(list(five_largest.largest_numbers()))
    [0, 1]
    >>> five_largest.append(2)
    >>> sorted(list(five_largest.largest_numbers()))
    [0, 1, 2]
    >>> five_largest.append(2)
    >>> sorted(list(five_largest.largest_numbers()))
    [0, 1, 2, 2]
    >>> five_largest.append(2)
    >>> sorted(list(five_largest.largest_numbers()))
    [0, 1, 2, 2, 2]
    >>> five_largest.append(0)
    >>> sorted(list(five_largest.largest_numbers()))
    [0, 1, 2, 2, 2]
    >>> five_largest.append(3)
    >>> sorted(list(five_largest.largest_numbers()))
    [1, 2, 2, 2, 3]
    >>> five_largest.append(-1)
    Traceback (most recent call last):
    ...
    five_largest.NegativaNumberAdded: -1

    """

    def __init__(self):
        maxlen = 5
        self._numbers = [-1] * maxlen

    def largest_numbers(self):
        return filter(lambda v: v >= 0, self._numbers)

    def append(self, n):
        if n < 0:
            raise NegativaNumberAdded(n)
        value_index_gen = ((value, index) for index, value in enumerate(self._numbers))
        min_value, min_index = min(value_index_gen)
        self._numbers[min_index] = max(min_value, n)


if __name__ == '__main__':
    five_largest = FiveLargest()
    while True:
        n = float(input('Type a number: '))
        try:
            five_largest.append(n)
        except NegativaNumberAdded:
            break
        else:
            print(list(five_largest.largest_numbers()))
