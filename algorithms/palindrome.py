s = "Was it a cat I saw?"
s2 = "Mathews"

# uses extra space of O(n)
# s = ''.join([i for i in s if i.isalpha()]).replace(' ','').lower()
# print(s)
# print(s == s[::-1])

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True

print(is_palindrome(s2))
