# A sequence of integers such that:
# x1 <= ... <= xk >= ... >= xn-1 for some k, 0 <= k < n
# For example:
#       1, 2, 3, 4, 5, 4, 3, 2, 1
# is a bitonic sequence. Write a program to find the largest
# element in such a sequence. In the above example, program
# should return 5.
# Note: Assume that such a peak exists

A1 = [1,2,3,4,5,4,3,2,1] # 5
A2 = [1,2,3,4,1] # 4
A3 = [1,6,5,4,3,2,1] # 6

def find_bitonic_peak_linear(A):
    peak = 0
    for val in A:
        peak = max(peak, val)
    return peak

def find_bitonic_peak_binary(A):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
    return None

print(find_bitonic_peak_binary(A2))
print(find_bitonic_peak_linear(A2))
