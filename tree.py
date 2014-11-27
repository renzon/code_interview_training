from collections import deque


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def deep_first(self):
        yield self
        if self.left is not None:
            yield from self.left.deep_first()
        if self.right is not None:
            yield from self.right.deep_first()

    def breadth_first(self):
        queue=deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)








    def __repr__(self):
        return 'Node(%r)' % self.value


def height(tree):
    if tree is None:
        return 0
    return 1 + max(height(tree.left), height(tree.right))

print('#### Heights')
print(height(None))  # expected 0
root = Node(0)
print(height(root))  # expected 1
root.left = Node(1)
print(height(root))  # expected 2
root.right = Node(2)

print(height(root))  # expected 2

root.right.left = Node(3)

print(height(root))  # expected 3
root.right.right = Node(5)

print(height(root))  # expected 3
root.right.left.left = Node(4)

print(height(root))  # expected 4


def deep_first_traversal(tree):
    if tree is None:
        return
    for node in tree.deep_first():
        print(node)


print('############### Deep First Traversal (')
deep_first_traversal(root)  # Expected 0, 1 , 2 , 3, 4, 5


def breadth_first_traversal(tree):
    if tree is None:
        return
    for node in tree.breadth_first():
        print(node)


print('############### Breadth First Traversal (')
breadth_first_traversal(root)  # Expected 0, 1 , 2 , 3, 5, 4