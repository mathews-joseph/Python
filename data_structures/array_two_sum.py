# Given a sorted array of integers, return the 2 numbers such that they would
# add upto a specific target. Assume that each input has exactly one solution
# and you may not use the same element twice.

# time complexity: O(n**2)
# space complexity: O(1)
def two_sum_brute_force(lst, target):
    """
    Brute force way to find the solution
    """
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                print(lst[i], lst[j])
                return True
    return False

# time complexity: O(n)
# space complexity: O(n)
def two_sum_dict(lst, target):
    map = {}
    for val in lst:
        if val in map:
            print(map[val], val)
            return True
        else:
            map[target - val] = val

# time complexity: O(n)
# space complexity: O(1)
def two_sum(lst, target):
    i = 0
    j = len(lst) - 1
    while i <= j:
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])
            return True
        elif lst[i] + lst[j] < target:
            i += 1
        elif lst[i] + lst[j] > target:
            j -= 1
    return False

def main():
    a = [-2, 1, 2, 4, 7, 11]
    target = 13
    two_sum_brute_force(a, target)
    two_sum_dict(a, target)
    two_sum(a,target)

if __name__ == "__main__":
    main()