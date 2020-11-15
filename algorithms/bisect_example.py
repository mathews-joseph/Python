# Bisect:
# Built in binary search in python

import bisect

A = [-14,-10,2,108,108,243,285,285,285,401]

# -10 is at index 1
# bisect_left returns the left most occurence
print(bisect.bisect_left(A,-10))

# bisect_right returns the insertion point to the
# right of the element in the list
print(bisect.bisect_right(A,-10))
# returns 9, because 8 is the last index of 285
print(bisect.bisect_right(A,285))

# insert elements such that the list still remains
# sorted
# insort_left will insert at the leftmost position
print(A)
bisect.insort_left(A,108)
print(A)