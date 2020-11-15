A = [2,3,3,5,7,11]
B = [3,3,7,15,31]

# A = set(A)
# B = set(B)
# print(A.intersection(B))

def sorted_array_intersection(A, B):
    i = j = 0
    intersection = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if not A[i] in intersection:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
    return intersection

print(sorted_array_intersection(A,B))