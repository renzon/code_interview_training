import heapq
from itertools import chain
from linked_list import _LinkedList, Node


class ListProxy():
    def __init__(self, lst, start=0, stop=None):
        self._stop = len(lst) if stop is None else stop
        self._start = start
        self._lst = lst

    def __getitem__(self, index):
        if isinstance(index, slice):
            slc = index
            start = self._start if slc.start is None else slc.start + self._start
            stop = self._stop if slc.stop is None else start + slc.stop
            return ListProxy(self._lst, start, stop)
        return self._lst[index + self._start]

    def __setitem__(self, key, value):
        self._lst[self._start + key] = value

    def bisect(self):
        middle = len(self) // 2
        return ListProxy(self._lst, self._start, self._start + middle), ListProxy(self._lst, self._start + middle,
                                                                                  self._stop)

    def __len__(self):
        return max(0, self._stop - self._start)

    def __iter__(self):
        return (self._lst[i] for i in range(self._start, self._stop))

    def __next__(self):
        return next(self)

    def __repr__(self):
        return 'ListProxy(%r, %r, %r)' % (self._lst, self._start, self._stop)


numbers = [1, 6, 2, 3, 4, 5]


def selection_sort(items):
    items = ListProxy(items)
    for i in range(len(items) - 1):
        j, min_element = min(enumerate(items[i:], i), key=lambda e: e[1])
        items[i], items[j] = min_element, items[i]
    return iter(items)


print('############# Selection Sort ##############')
print(list(selection_sort([])))
print(list(selection_sort([1])))
print(list(selection_sort(numbers)))


def insertion_sort(items):
    if not items:
        return items
    items = items[:]
    sorted_linked_list = _LinkedList()
    sorted_linked_list.insert(0, Node(items.pop()))

    def insert(e):
        ahead_iter = iter(sorted_linked_list)
        first_item = next(ahead_iter)
        if e < first_item.value:
            sorted_linked_list.insert(0, Node(e))
        else:
            current_iter = iter(sorted_linked_list)
            for previous_node, node in zip(current_iter, ahead_iter):
                if e < node.value:
                    previous_node.next = Node(e, node)
                    return
            last_node = next(current_iter)
            last_node.next = Node(e)

    while items:
        insert(items.pop())
    return (node.value for node in sorted_linked_list)


print('############# Insertion Sort ##############')
print(list(insertion_sort([])))
print(list(insertion_sort([1])))

print(list(insertion_sort(numbers)))


def quick_sort(items):
    if len(items) < 2:
        return iter(items)
    items = ListProxy(items)

    def _quick_sort(inner_items):
        pivot_index = len(inner_items) // 2
        pivot = inner_items[pivot_index]
        left = []
        right = []
        for value in chain(inner_items[:pivot_index], inner_items[pivot_index + 1:]):
            if value < pivot:
                left.append(value)
            else:
                right.append(value)
        return chain(quick_sort(left), [pivot], quick_sort(right))

    return _quick_sort(items)


print('############# Quick ##############')
print(list(quick_sort([])))
print(list(quick_sort([1])))

print(list(quick_sort(numbers)))


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

leaves_on_memory = 0

def print_memory():
    print('Leaves: %s' % leaves_on_memory)

def merg_rec(items):
    if len(items) < 2:
        global leaves_on_memory
        leaves_on_memory += 1
        print_memory()
        yield from iter(items)
        leaves_on_memory -= 1
        print_memory()
    else:
        middle = len(items) // 2
        left_middle, right_middle = items[:middle], items[middle:]
        yield from heapq.merge(merg_rec(left_middle), merg_rec(right_middle))


def merge_sort(items):
    list_proxy = ListProxy(items)
    return [i for i in merg_rec(list_proxy)]


print('############ Merge Sort ###################')

print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([2, 1]))
print(merge_sort(numbers))
