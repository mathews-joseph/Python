class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Node doesn't exist")
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        # node to delete is the head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if not cur_node:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        # if position is head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if not cur_node:
            return
        prev.next = cur_node.next
        cur_node = None

    def swap_nodes(self, k1, k2):
        if k1 == k2:
            return

        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != k1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != k2:
            prev2 = cur2
            cur2 = cur2.next

        if not cur1 or not cur2:
            return

        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        cur1.next, cur2.next = cur2.next, cur1.next

    def reverse_list(self):
        prev = None
        cur = self.head
        # A -> B -> C
        while cur:          # cur = A             \ cur = B
            nxt = cur.next  # nxt = B             \ nxt = C
            cur.next = prev # None <- A    B -> C \ None <- A <- B    C
            prev = cur      # prev = A            \ prev = B
            cur = nxt       # cur = B             \ nxt = C
        self.head = prev

    def reverse_list_recursive(self):
        def _reverse(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse(cur, prev)

        self.head = _reverse(cur=self.head, prev=None)

    def merge_2_ll(self, l2):
        # literally merging the 2 linked lists
        # no extra space is used
        new_head = tracker = None
        p = self.head
        q = l2.head
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data < q.data:
                new_head = tracker = p
                p = p.next
            else:
                new_head = tracker = q
                q = q.next
        while p and q:
            if p.data < q.data:
                tracker.next = p
                tracker = p
                p = p.next
            else:
                tracker.next = q
                tracker = q
                q = q.next

        if not p:
            tracker.next = q
        if not q:
            tracker.next = p

        self.head = new_head
        l2.head = None

    def sum_2_ll(self, l2):
        p = self.head
        q = l2.head
        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
                p = p.next
            if not q:
                j = 0
            else:
                j = q.data
                q = q.next
            result = i + j + carry
            if result > 9:
                carry = 1
                result = result % 10
            sum_list.append(result)
        sum_list.print_list()

    def rotate(self, k):
        cur = self.head
        prev = None
        count = 0
        while cur and count < k:
            count += 1
            prev = cur
            cur = cur.next
        p = q = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    def move_tail_to_head(self):
        q = self.head
        prev = None
        while q.next:
            prev = q
            q = q.next
        q.next = self.head
        prev.next = None
        self.head = q

    def remove_duplicates(self):
        check = set()
        prev = None
        cur = self.head
        while cur:
            if cur.data in check:
                prev.next = cur.next
                cur = None
            else:
                check.add(cur.data)
                prev = cur
            cur = prev.next

    def count_occurences(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def is_palindrome(self):
        # method 1:
        # s = ''
        # cur = self.head
        # while cur:
        #     s += cur.data
        #     cur = cur.next
        # return s == s[::-1]

        # method 2:
        # cur = self.head
        # res = []
        # while cur:
        #     res.append(cur.data)
        #     cur = cur.next
        # cur = self.head
        # while cur:
        #     if cur.data != res.pop():
        #         return False
        #     cur = cur.next
        # return True

        # method 3
        p = self.head
        q = self.head
        nodes = []
        while q:
            nodes.append(q)
            q = q.next
        count = 0
        while count < len(nodes)//2:
            if nodes.pop().data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def length_recursive(self, node):
        if not node:
            return 0
        return 1 + self.length_recursive(node.next)

    def print_nth_from_last(self, n):
        # method 1
        # length = self.length()
        # cur = self.head
        # while cur:
        #     if length == n:
        #         return cur.data
        #     length -= 1
        #     cur = cur.next
        # return None

        # method 2
        p = q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            return None
        while p and q:
            p = p.next
            q = q.next
        return p.data

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

if __name__ == "__main__":
    # ll = LinkedList()
    # ll.append("A")
    # ll.append("B")
    # ll.append("C")
    # ll.append("D")

    # ll.insert_after(ll.head.next, "E")

    # ll.delete_node("B")
    # ll.print_list()

    # ll.delete_node_at_pos(1)
    # ll.print_list()

    # print(ll.length())
    # print(ll.length_recursive(ll.head))

    # ll.swap_nodes("B", "C")
    # ll.swap_nodes("A", "B")

    # ll.reverse_list()
    # ll.reverse_list_recursive()
    # ll.print_list()

    # l1 = LinkedList()
    # l1.append(1)
    # l1.append(5)
    # l1.append(7)
    # l1.append(9)
    # l1.append(10)
    # l1.print_list()
    # print()
    # l2 = LinkedList()
    # l2.append(2)
    # l2.append(3)
    # l2.append(4)
    # l2.append(6)
    # l2.append(8)
    # l2.print_list()
    # print()
    # l1.merge_2_ll(l2)
    # l1.print_list()
    # print()
    # l2.print_list()

    # l1 = LinkedList()
    # l1.append(1)
    # l1.append(6)
    # l1.append(1)
    # l1.append(4)
    # l1.append(2)
    # l1.append(2)
    # l1.append(4)
    # l1.remove_duplicates()
    # l1.print_list()

    # print(ll.print_nth_from_last(2))

    # l1 = LinkedList()
    # l1.append(1)
    # l1.append(2)
    # l1.append(1)
    # l1.append(3)
    # l1.append(1)
    # l1.append(4)
    # l1.append(1)
    # print(l1.count_occurences(1))
    # print(l1.count_occurences_recursive(l1.head, 1))

    # l1 = LinkedList()
    # l1.append(1)
    # l1.append(2)
    # l1.append(3)
    # l1.append(4)
    # l1.append(5)
    # l1.append(6)
    # l1.rotate(4)
    # l1.print_list()

    # l1 = LinkedList()
    # l1.append("R")
    # l1.append("A")
    # l1.append("D")
    # l1.append("A")
    # l1.append("R")

    # l2 = LinkedList()
    # l2.append("A")
    # l2.append("B")
    # l2.append("C")

    # print(l1.is_palindrome())
    # print(l2.is_palindrome())

    # ll.move_tail_to_head()
    # ll.print_list()

    l1 = LinkedList()
    l1.append(5)
    l1.append(6)
    l1.append(3)

    l2 = LinkedList()
    l2.append(8)
    l2.append(4)
    l2.append(2)

    print(365 + 248)
    l1.sum_2_ll(l2)