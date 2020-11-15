def merge_sort(lst):
    if len(lst) > 1:
        m = len(lst) // 2
        left = lst[:m]
        right = lst[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        lst = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                lst.append(left[0])
                left.pop(0)
            else:
                lst.append(right[0])
                right.pop(0)

        for i in left:
            lst.append(i)

        for i in right:
            lst.append(i)

    return lst

print(merge_sort([10,4,2,7,12,5]))