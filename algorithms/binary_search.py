data = [1,2,3,4,5,6,7,8,9,10]
target = 1

def linear_search(lst, target):
    for i in lst:
        if i == target:
            return True
    return False

def binary_search_iterative(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def binary_search_recursive(lst, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if target == lst[mid]:
        return True
    elif target > lst[mid]:
        return binary_search_recursive(lst, target, mid+1, high)
    else:
        return binary_search_recursive(lst, target, low, mid-1)

print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))