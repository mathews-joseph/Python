from linked_list import LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        cur = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = Node(data)
            cur.next.next = self.head

    def remove(self, key):
        if self.head.data == key and self.head.next == self.head:
            self.head = None
        elif self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def remove_node(self, node):
        if self.head == node and self.head.next == self.head:
            self.head = None
        elif self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def split_list(self):
        length = len(self)
        if length == 0:
            return
        if length == 1:
            return self.head
        mid = length // 2
        count = 0
        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cl = CircularLinkedList()
        while cur.next != self.head:
            split_cl.append(cur.data)
            cur = cur.next
        split_cl.append(cur.data)

        self.print_list()
        print()
        split_cl.print_list()

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def josephus_circle(self, step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            self.remove_node(cur)
            cur = cur.next

    def is_circular_ll(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

if __name__ == "__main__":
    # c = CircularLinkedList()
    # c.append("A")
    # c.append("B")
    # c.append("C")
    # c.append("D")
    # c.print_list()
    # print()

    # c.prepend("1")
    # c.prepend("0")
    # c.print_list()
    # print()

    # c.remove("0")
    # c.remove("1")
    # c.print_list()
    # print()

    # print(len(c))
    # c.split_list()

    # c = CircularLinkedList()
    # c.append(1)
    # c.append(2)
    # c.append(3)
    # c.append(4)
    # c.josephus_circle(2)
    # c.print_list()
    # print()

    c = CircularLinkedList()
    c.append(1)
    c.append(2)
    c.append(3)
    c.append(4)
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    print(c.is_circular_ll(c))
    print(c.is_circular_ll(l))