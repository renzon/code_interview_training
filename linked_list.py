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
            for i, next_node in enumerate(it, 1):
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


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)

for i in linked_list:
    print(i)

linked_list.insert(0, 3)
linked_list.insert(3, 4)
linked_list.insert(2, 5)

print('######## Lista after insertions')
for i in linked_list:
    print(i)         
            
            
            
            
            
            
        