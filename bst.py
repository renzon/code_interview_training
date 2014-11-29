class BinarySearchTree():
    def __init__(self):
        self._tree = []

    def left(self, i):
        i = 2 * i + 1
        return i, self.node(i)

    def right(self, i):
        i = 2 * i + 2
        return i, self.node(i)

    def parent(self, i):
        i = (i - 1) // 2
        return i, self.node(i)

    def node(self, i):
        if 0 <= i < len(self._tree):
            return self._tree[i]

    def swap(self, i, j):
        self._tree[i], self._tree[j] = self._tree[j], self._tree[i]

    def move_down(self, n_idx):
        node = self.node(n_idx)
        while node is not None:
            l_idx, left = self.left(n_idx)
            if left is None:
                return n_idx
            r_idx, right = self.right(n_idx)
            if right is None:
                if left > node:
                    self.swap(n_idx, l_idx)
                    return l_idx
                return n_idx
            if left <= node <= right:
                return n_idx
            elif left > node:
                self.swap(n_idx, l_idx)
                n_idx = l_idx
            else:
                self.swap(n_idx, r_idx)
                n_idx = r_idx

    def append(self, element):
        e_index = len(self._tree)  # element = 2    e_index = 2   _tree = [1, 0, 2]
        self._tree.append(element)
        if len(self._tree) == 1:
            return 0
        p_index, p_element = self.parent(e_index)  # p_index = -1   p_element = None

        # moving new element up keeping the tree balanced
        while p_element is not None:
            self.swap(e_index, p_index)
            self.move_down(e_index)
            e_index = p_index
            p_index, p_element = self.parent(e_index)

        return self.move_down(0)


    def inorder_traversal(self):  # bst_tree =[1, 0, 2]
        if not self._tree:
            return
        stack = []
        stack.append((0, self.node(0)))

        # stack = [], c_index = 2, c_node = 2, l_index = 5, left = None

        while stack:
            c_index, c_node = stack.pop()

            l_index, left = self.left(c_index)
            if left is None:
                yield c_node
                if stack:
                    _, node = stack.pop()
                    yield node
            else:
                r_index, right = self.right(c_index)  # r_index = 2, right = 2
                if right:
                    stack.append((r_index, right))
                    stack.append((c_index, c_node))
                    stack.append((l_index, left))
                else:
                    yield left
                    yield c_node
                    if stack:
                        _, node = stack.pop()
                        yield node


if __name__ == '__main__':
    import unittest

    class BSTTests(unittest.TestCase):
        def test_append(self):
            bst = BinarySearchTree()
            self.assertListEqual([], bst._tree)
            bst.append(0)
            self.assertListEqual([0], bst._tree)
            bst.append(1)
            self.assertListEqual([1, 0], bst._tree)
            bst.append(2)
            self.assertListEqual([1, 0, 2], bst._tree)
            bst.append(3)
            self.assertListEqual([2, 1, 3, 0], bst._tree)
            bst.append(4)
            self.assertListEqual([3, 1, 4, 0, 2], bst._tree)
            bst.append(5)
            self.assertListEqual([4, 1, 5, 0, 2, 3], bst._tree)
            bst.append(-1)
            self.assertListEqual([1, 0, 4, -1, 2, 3, 5], bst._tree)
            bst.append(-2)
            self.assertListEqual([1, 0, 4, -1, 2, 3, 5, -2], bst._tree)

        def test_inorder_traversal(self):
            bst = BinarySearchTree()
            self.assertListEqual([], [i for i in bst.inorder_traversal()])
            bst.append(0)
            self.assertListEqual([i for i in range(1)], [i for i in bst.inorder_traversal()])
            bst.append(1)
            self.assertListEqual([i for i in range(2)], [i for i in bst.inorder_traversal()])
            bst.append(2)
            self.assertListEqual([i for i in range(3)], [i for i in bst.inorder_traversal()])
            bst.append(3)
            self.assertListEqual([i for i in range(4)], [i for i in bst.inorder_traversal()])
            bst.append(4)
            self.assertListEqual([i for i in range(5)], [i for i in bst.inorder_traversal()])
            bst.append(5)
            self.assertListEqual([i for i in range(6)], [i for i in bst.inorder_traversal()])
            bst.append(6)
            self.assertListEqual([i for i in range(7)], [i for i in bst.inorder_traversal()])

    unittest.main()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
                
                
                
                
                