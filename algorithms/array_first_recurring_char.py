def first_recurring(a):
    check = set()
    for char in a:
        if char in check:
            return char
        check.add(char)
    return None

print(first_recurring("abc"))