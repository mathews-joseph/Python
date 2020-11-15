s1 = "fairy tales"
s2 = "rail safety"

# extra space complexity of O(n)
# time complexity of O(nlogn) because of the sorting algorithm
# s1 = sorted(s1.replace(' ', '').lower())
# s2 = sorted(s2.replace(' ', '').lower())
# print(s1 == s2)

def is_anagram(s1, s2):
    count = {}

    if len(s1) != len(s2):
        return False

    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in s2:
        if ch in count:
            count[ch] -= 1
        else:
            return False

    for keys in count:
        if count[keys] != 0:
            return False

    return True

print(is_anagram(s1,s2))