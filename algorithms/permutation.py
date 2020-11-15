is_perm_1 = "god"
is_perm_2 = "dog"

not_perm_1 = "not"
not_perm_2 = "top"

# time: O(nlogn)
# space: O(1)
def is_perm_f1(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1.lower())
    s2 = sorted(s2.lower())
    return s1 == s2

# time: O(n)
# space: O(n)
def is_perm_f2(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()
    check = {}
    for ch in s1:
        if ch in check:
            check[ch] += 1
        else:
            check[ch] = 1

    for ch in s2:
        if ch in check:
            check[ch] -= 1
        else:
            return False

    return True

print(is_perm_f1(is_perm_1, is_perm_2))
print(is_perm_f1(not_perm_1, not_perm_2))

print(is_perm_f2(is_perm_1, is_perm_2))
print(is_perm_f2(not_perm_1, not_perm_2))