# fixed point is an index where, index == array[index]

A1 = [-10,-5,0,3,7] # 3
A2 = [0,2,5,8,17] # 0
A3 = [-10,-5,3,4,7,9] # none

# time: O(n)
# space: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

# array is sorted and no duplicate values
def find_fixed_point_binary(A):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None

print(find_fixed_point_linear(A1))
print(find_fixed_point_binary(A1))
print(find_fixed_point_linear(A2))
print(find_fixed_point_binary(A2))
print(find_fixed_point_linear(A3))
print(find_fixed_point_binary(A3))