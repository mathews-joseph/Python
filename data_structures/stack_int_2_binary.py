"""
Use a stack to convert an integer
to binary
"""

from stack import Stack

def int_2_binary(n):
    s = Stack()
    while n > 0:
        rem = n % 2
        s.push(rem)
        n //= 2
    res = ''
    while not s.is_empty():
        res += str(s.pop())

    return res

print(int_2_binary(4))