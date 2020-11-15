class Node:
    """
    A class that implements the nodes in a binary tree
    """
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    A class that implements the binary search tree
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left:
                self._insert(data, cur_node.left)
            else:
                cur_node.left = Node(data)
        elif data > cur_node.data:
            if cur_node.right:
                self._insert(data, cur_node.right)
            else:
                cur_node.right = Node(data)
        else:
            print("Duplicate value")

    def find(self, data):
        if self.root:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, cur_node):
        if data == cur_node.data:
            return True
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        else:
            return False

    def inorder_print(self):
        if self.root:
            self._inorder_print(self.root)
        else:
            print("no tree")

    def _inorder_print(self, cur_node):
        if cur_node:
            self._inorder_print(cur_node.left)
            print(cur_node.data)
            self._inorder_print(cur_node.right)

    def is_bst(self):
        if self.root:
            is_bst_flag = self._is_bst(self.root)
            if is_bst_flag is None:
                return True
            return False
        return True

    def _is_bst(self, cur_node):
        if cur_node.left:
            if cur_node.left.data < cur_node.data:
                return self._is_bst(cur_node.left)
            else:
                return False
        if cur_node.right:
            if cur_node.right.data > cur_node.data:
                return self._is_bst(cur_node.right)
            else:
                return False

"""
A valid binary search tree because we make use of the insert method
"""
bst = BST()
bst.insert(4)
bst.insert(6)
bst.insert(1)
bst.insert(7)
bst.insert(10)
bst.insert(12)
bst.insert(3)

print(bst.find(10))

"""
An invalid binary search tree
"""
bt = BST()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)


bst.inorder_print()
print()
bt.inorder_print()
print()
print(bst.is_bst())
print(bt.is_bst())