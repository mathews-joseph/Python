unique_str = "AbCDefG"
not_unique_str = "non unique str"

def normalize(s):
    return s.replace(' ', '').lower()

def is_unique_1(s):
    check = {}
    s = normalize(s)
    for ch in s:
        if ch in check:
            return False
        else:
            check[ch] = 1
    return True

def is_unique_2(s):
    s = normalize(s)
    return len(set(s)) == len(s)

def is_unique_3(s):
    s = normalize(s)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for ch in s:
        if ch in alpha:
            alpha = alpha.replace(ch,'')
        else:
            return False
    return True

print(is_unique_1(unique_str))
print(is_unique_1(not_unique_str))

print(is_unique_2(unique_str))
print(is_unique_2(not_unique_str))

print(is_unique_3(unique_str))
print(is_unique_3(not_unique_str))