class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)

    def preorder_print(self, node):
        if node:
            print(node.val)
            self.preorder_print(node.left)
            self.preorder_print(node.right)

    def inorder_print(self, node):
        if node:
            self.inorder_print(node.left)
            print(node.val)
            self.inorder_print(node.right)

    def postorder_print(self, node):
        if node:
            self.postorder_print(node.left)
            self.postorder_print(node.right)
            print(node.val)

    def levelorder_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.items:
            cur = q.dequeue()
            print(cur.val)
            if cur.left:
                q.enqueue(cur.left)
            if cur.right:
                q.enqueue(cur.right)

    def reverse_levelorder_print(self, node):
        if node:
            q = Queue()
            s = Stack()
            q.enqueue(node)
            while q.items:
                cur = q.dequeue()
                s.push(cur)
                if cur.right:
                    q.enqueue(cur.right)
                if cur.left:
                    q.enqueue(cur.left)
            while s.items:
                print(s.pop().val)

    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_recursive(self, node):
        """
        The recursive way to find the size of the b-tree
        """
        if not node:
            return 0
        left_size = self.size_recursive(node.left)
        right_size = self.size_recursive(node.right)
        return 1 + left_size + right_size

    def size(self):
        """
        The iterative way to find the size of the b-tree
        """
        size = 0
        if self.root:
            s = Stack()
            s.push(self.root)
            while s.items:
                node = s.pop()
                size += 1
                if node.left:
                    s.push(node.left)
                if node.right:
                    s.push(node.right)
        return size

#           1
#       /     \
#     2        3
#   /  \     /  \
#  4    5   6    7

bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

# bt.preorder_print(bt.root)
# print("")
# bt.inorder_print(bt.root)
# print("")
# bt.postorder_print(bt.root)
# print("")
# bt.levelorder_print(bt.root)
# print("")
# bt.reverse_levelorder_print(bt.root)
# print("")
# print(bt.height(bt.root))
print(bt.size())

print(bt.size_recursive(bt.root.left.left))