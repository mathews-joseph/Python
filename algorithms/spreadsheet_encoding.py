def ss_encoder(s):
    sum = 0
    count = len(s) - 1
    for ch in s:
        sum += (26**count) * (ord(ch) - ord("A") + 1)
        count -= 1
    return sum

print(ss_encoder("A"))
print(ss_encoder("AA"))
print(ss_encoder("ZZ"))