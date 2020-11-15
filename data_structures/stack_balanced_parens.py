"""
Use a stack to check if a string has
balanced usage of paranthesis.
Examples:
    (), ()(), (({{[]}})) - Balanced
    ((), {{{)}], [][]]]  - Not Balanced
"""

from stack import Stack

def is_match(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    idx = 0
    is_balanced = True
    while idx < len(paren_string) and is_balanced:
        paren = paren_string[idx]
        if paren in '({[':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
        idx += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print(is_paren_balanced('(()'))