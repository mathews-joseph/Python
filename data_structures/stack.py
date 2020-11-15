"""
stack data structure
Insertion (push) and deletion (pop) happen at the top
Peek is similar to pop but without removal of the element
LIFO - Last In Fast Out
top -> D
       C
       B
       A

using a list:
  0    1    2    3
['A', 'B', 'C', 'D']
                 ^
            top _|
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def get_stack(self):
        return self.items

def main():
    s = Stack()
    print(s.is_empty())
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")
    print(s.peek())
    print(s.get_stack())

if __name__ == "__main__":
    main()
