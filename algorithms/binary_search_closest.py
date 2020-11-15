A1 = [1,2,4,5,6,6,8,9]
A2 = [2,5,6,7,8,8,9]

def find_closest_number(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    result = None

    if len(A) == 0:
        return result
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2
        if min_diff < abs(target - A[mid]):
            min_diff = abs(target - A[mid])
            result = A[mid]

        if mid + 1 < len(A):
            min_diff_right = abs(target - A[mid + 1])
        if mid > 0:
            min_diff_left = abs(target - A[mid - 1])

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            result = A[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            result = A[mid + 1]

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            return A[mid]
    return result

print(find_closest_number(A1, 11))