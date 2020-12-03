class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return 'Node(%r, %r)' % (self.value, self.next)


class _NodeIterator():
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration()
        node = self.node
        self.node = node.next
        return node


class _LinkedList():
    def __init__(self):
        self._first_node = None
        self._len = 0


    def __len__(self):
        return self._len

    def __iter__(self):
        return _NodeIterator(self._first_node)

    def pop(self, index=None):
        poped = None  # poped = None self= 3, 5, 2, 4 index=None
        if len(self) == 0:
            raise IndexError('Can not pop a_com_fatia_linar item from a_com_fatia_linar empty linked list')
        if index is None:
            index = len(self) - 1  # index= 3
        if index == 0:
            poped = self._first_node
            self._first_node = poped.next
        elif index < len(self):
            ite = iter(self)
            previous = next(ite)  # previous = 2
            for i, node in enumerate(ite, 1):  # 3, 4
                if i == index:
                    previous.next = node.next
                    poped = node  # poped = 4
                    break
                previous = node
        else:
            raise IndexError
        self._len -= 1  # 4
        return poped  # 1

    def insert(self, index, node):
        if index == 0 and len(self) == 0:
            self._first_node = node
        elif index == 0:
            node.next = self._first_node
            self._first_node = node
        elif index > len(self):
            return IndexError
        elif index == len(self):
            i = iter(self)
            last_node = next(i)
            for n in i:
                last_node = n
            last_node.next = node
        else:
            it = iter(self)
            previous_node = next(it)
            for i, next_node in enumerate(it,1):
                if i == index:
                    previous_node.next = node
                    node.next = next_node
                    break
                previous_node = next_node

        self._len += 1


class LinkedList():
    def __init__(self):
        self._linked_list = _LinkedList()

    def __iter__(self):
        return (n.value for n in iter(self._linked_list))

    def __len__(self):
        return len(self._linked_list)

    def insert(self, index, value):
        self._linked_list.insert(index, Node(value))

    def append(self, value):
        self.insert(len(self), value)

    def pop(self, index=None):
        return self._linked_list.pop(index).value


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)

for i in linked_list:
    print(i)
# 1, 2            
linked_list.insert(0, 3)  # 3, 1, 2
linked_list.insert(3, 4)  # 3, 1, 2, 4
linked_list.insert(2, 5)  # 3, 1, 5, 2, 4

print('###### List after insertions')

for i in linked_list:
    print(i)

print('###### List second element')

linked_list.pop(1)  # 3, 1, 5, 2, 4

for i in linked_list:
    print(i)

print('###### List last element')

linked_list.pop()  # 3, 5, 2, 4

for i in linked_list:
    print(i)

print('###### List first element')

linked_list.pop(1)

for i in linked_list:
    print(i)             

            
            
            
            
            
        