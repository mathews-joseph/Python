def str_to_int(s):
    num = 0
    idx = 0
    is_neg = False
    if s[0] == '-':
        idx = 1
        is_neg = True
    for i in range(idx, len(s)):
        num += 10**(len(s) - (i+1))*(ord(s[i]) - ord('0'))
    if is_neg:
        num *= -1
    return num

print(str_to_int('-123'))
print(str_to_int('321'))