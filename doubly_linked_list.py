# Flatenning problem from Programming Interviews Exposed

class Node():
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.child = None
        self.value = value

    def clone_value_and_child(self):
        node = Node(self.value)
        node.child = self.child
        return node


    def append(self, node):
        node.next = self.next
        node.previous = self
        self.next = node
        if node.next:
            node.next.previous = node


class DoubleLinkedList():
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            try:
                first_item = next(iter(iterable))
                has_nodes = isinstance(first_item, Node)
                if not has_nodes:
                    iterable = (Node(i) for i in iterable)
                for node in iterable:
                    self.append(node)
            except StopIteration:
                pass

    def __iter__(self):
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                yield current_node
                current_node = current_node.next

    def __reversed__(self):
        if self.tail is not None:
            current_node = self.tail
            while current_node is not None:
                yield current_node
                current_node = current_node.previous


    def flatenning(self):
        for node in iter(self):
            yield node
            linked_list = DoubleLinkedList()
            linked_list.head = node.child
            linked_list.tail = node.child
            yield from linked_list.flatenning()

    def unflatenning(self):
        unflated_list = DoubleLinkedList()
        it = iter(self)
        try:
            current_node = next(it)
            cloned_node = Node(current_node.value)
            unflated_list.append(cloned_node)
            while True:
                next_node = next(it)
                next_clone = Node(next_node.value)
                if current_node.child is None:
                    cloned_node.append(next_clone)
                else:
                    cloned_node.child = next_clone
                current_node = next_node
                cloned_node = next_clone
        except StopIteration:
            pass
        return unflated_list

    def items_flatenning(self):
        return (node.value for node in self.flatenning())

    def items(self):
        return (node.value for node in iter(self))

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.append(node)
        self.tail = node


r = [Node(i) for i in range(1, 4)]
node_0 = r[0]

node_0.child = Node(4)
node_0.child.child = Node(5)
node_0.child.child.append(Node(6))

r[1].child = Node(7)
doubly_linked_list = DoubleLinkedList(r)

print(list(n.value for n in reversed(doubly_linked_list)))
print(list(doubly_linked_list.items_flatenning()))

flatenned_list = DoubleLinkedList()

for node in doubly_linked_list.flatenning():
    flatenned_list.append(node.clone_value_and_child())

print(list(node.value for node in flatenned_list))
print(list(node.value for node in flatenned_list.unflatenning().flatenning()))
print(list(node.value for node in flatenned_list.unflatenning()))