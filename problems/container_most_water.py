def maxArea(height):
    max_area = 0
    head = 0
    tail = len(height) - 1
    while head < tail:
        max_area = max(max_area, (tail-head)*min(height[head],height[tail]))
        if height[tail] < height[head]:
            tail -= 1
        elif height[head] < height[tail]:
            head += 1

    return max_area

# print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([2,3,4,5,18,17,6]))
# print(maxArea([4,3,2,1,4]))
# print(maxArea([1,2,1]))
# print(maxArea([1,1]))