k = 300

# time: O(n)
def find_(k):
    i = 1
    while i <= k**(0.5):
        i += 1
    return i-1

def find(k):
    low = 0
    high = k
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

print(find(k))