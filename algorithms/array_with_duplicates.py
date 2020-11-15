# an array of sorted integers
# return index of first occurence of target

A = [-14,-10,2,108,108,243,285,285,285,401]
target = 285

# time: O(n)
def find_(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i
    return None

def find(A, target):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid-1] != target:
                return mid
            high = mid - 1
    return None

print(find(A,target))