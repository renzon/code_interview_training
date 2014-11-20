import heapq

numbers = [1, 6, 2, 3, 4, 5]


def selection_sort(items):
    items = items[:]
    for i in range(len(items) - 1):
        j, min_element = min(enumerate(items[i:], i), key=lambda e: e[1])
        items[i], items[j] = min_element, items[i]
    return items


print(selection_sort([]))
print(selection_sort([1]))
print(selection_sort(numbers))


def insertion_sort(items):
    if not items:
        return items
    items = items[:]
    sorted_list = [items.pop()]

    def insert(e):
        for i, value in enumerate(sorted_list):
            if e < value:
                sorted_list.insert(i, e)
                return
        sorted_list.append(e)

    while items:
        insert(items.pop())
    return sorted_list


print(insertion_sort([]))
print(insertion_sort([1]))
print(insertion_sort(numbers))


def quick_sort(items):
    if len(items) < 2:
        return items
    pivot_index = len(items) // 2
    pivot = items[pivot_index]
    left = []
    right = []
    for value in items[:pivot_index] + items[pivot_index + 1:]:
        if value < pivot:
            left.append(value)
        else:
            right.append(value)
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([]))
print(quick_sort([1]))
print(quick_sort(numbers))


class ListProxy():
    def __init__(self, lst, start=0, stop=None):
        self._stop = len(lst) if stop is None else stop
        self._start = start
        self._lst = lst

    def __getitem__(self, index):
        return self._lst[index + self._start]

    def bisect(self):
        middle = len(self) // 2
        return ListProxy(self, 0, middle), ListProxy(self, middle)

    def __len__(self):
        return max(0, self._stop - self._start)

    def __iter__(self):
        return (self[i] for i in range(len(self)))

    def __next__(self):
        return next(self)

    def __repr__(self):
        return 'ListProxy(%r, %r, %r)' % (self._lst, self._start, self._stop)


def merg_rec(items):
    if len(items) < 2:
        yield from iter(items)
    else:
        left_middle, right_middle = items.bisect()
        yield from heapq.merge(merg_rec(left_middle), merg_rec(right_middle))


def merge_sort(items):
    list_proxy = ListProxy(items)
    return [i for i in merg_rec(list_proxy)]


print('############ Merge Sort ###################')

print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([2, 1]))
print(merge_sort(numbers))
