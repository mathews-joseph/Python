def next_number(s):
    res = ''
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        res += str(count) + s[i]
        i += 1
    return res

n = 4
s = '1'
print(s)
for i in range(n-1):
    s = next_number(s)
    print(s)