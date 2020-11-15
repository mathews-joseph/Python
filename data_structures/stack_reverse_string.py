from stack import Stack

def reverse_string(input_string):
    s = Stack()
    for ch in input_string:
        s.push(ch)
    res = ''
    while s.items:
        res += s.pop()
    return res

print(reverse_string("mathews"))