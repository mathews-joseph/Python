class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if not cur.next and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = cur
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if not cur.prev and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                cur.prev = new_node
                new_node.prev = prev
                prev.next = new_node
                new_node.next = cur
            cur = cur.next

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # case 1: only head exists
                if not cur.next:
                    self.head = None
                    return
                # case 2: node to delete is head but there are items
                else:
                    self.head = cur.next
                    self.head.prev = None
                    cur = None
                    return
            elif cur.data == key:
                # case 3: middle node is deleted
                if cur.next:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur = None
                    return
                # case 4: last node is deleted
                else:
                    cur.prev.next = None
                    cur = None
                    return

            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # case 1: only head exists
                if not cur.next:
                    self.head = None
                    return
                # case 2: node to delete is head but there are items
                else:
                    self.head = cur.next
                    self.head.prev = None
                    cur = None
                    return
            elif cur == node:
                # case 3: middle node is deleted
                if cur.next:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur = None
                    return
                # case 4: last node is deleted
                else:
                    cur.prev.next = None
                    cur = None
                    return

            cur = cur.next

    def reverse(self):
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.next, cur.prev = cur.prev, cur.next
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        check = set()
        cur = self.head
        while cur:
            if cur.data in check:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
            else:
                check.add(cur.data)
                cur = cur.next

    def pairs_with_sum(self, target):
        pairs = []
        seen = set()
        cur = self.head
        while cur:
            req = target - cur.data
            if req in seen:
                pairs.append((req, cur.data))
            else:
                seen.add(cur.data)
            cur = cur.next
        return pairs

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


if __name__ == "__main__":
    # d = DoublyLinkedList()
    # d.append(1)
    # d.append(2)
    # d.append(3)
    # d.append(4)
    # d.prepend(0)
    # d.add_after_node(4,6)
    # d.add_before_node(6,5)
    # d.print_list()
    # print()

    # d.delete(6)
    # d.delete(3)
    # d.print_list()
    # print()

    # d.reverse()
    # d.print_list()

    # d = DoublyLinkedList()
    # d.append(8)
    # d.append(4)
    # d.append(6)
    # d.append(4)
    # d.append(8)
    # d.append(4)
    # d.append(10)
    # d.append(12)
    # d.append(12)
    # d.print_list()
    # print()
    # d.remove_duplicates()
    # d.print_list()

    d = DoublyLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    d.append(5)
    d.print_list()
    print(d.pairs_with_sum(0))