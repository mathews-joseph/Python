palin_perm = "Tact Coa" # t a c o c a t
not_palin_perm = "This is not a palindrome permutation"

# time: O(n)
# space: O(n)
def is_palin_perm(s):
    result = {}
    processed_str = s.replace(' ', '').lower()
    for ch in processed_str:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

    odd_count = 0
    for val in result.values():
        if val % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif val % 2 != 0 and odd_count != 0:
            return False

    return True

# print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))