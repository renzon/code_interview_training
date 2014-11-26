class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def deep_first(self):
        if self.left is not None:
            yield self.left
            yield from self.left.deep_first()
        if self.right is not None:
            yield self.right
            yield from self.right.deep_first()


    def __repr__(self):
        return 'Node(%r)' % self.value


def height(tree):
    if tree is None:
        return 0
    return 1 + max(height(tree.left), height(tree.right))


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
    print(tree)
    for node in tree.deep_first():
        print(node)


deep_first_traversal(root)  # Expected 0, 1 , 2 , 3, 4, 5