# c = {'a': 1, 'b': 4, 'c': 2}
# print(sorted(c.items(), key=lambda x: x[1], reverse=False))

def partition(arr, low, high):
    small = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            small += 1
            arr[small], arr[j] = arr[j], arr[small]

    arr[small+1],arr[high] = arr[high], arr[small+1]
    return small+1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr,0,len(arr)-1)
print(arr)