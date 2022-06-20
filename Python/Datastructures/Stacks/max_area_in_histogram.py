def max_area(arr):
    stack = []
    stack.append(-1)
    maxarea = 0
    for i in range(len(arr)):
        while stack[-1]!= -1 and stack[-1] >= arr[i]:
            right = i
            top = stack.pop()
            left = stack[-1]
            area = arr[top] * (right-left-1)
            maxarea = max(maxarea,area)
        stack.append(i)
    while stack[-1]!= -1:
        right = len(arr)
        top = stack.pop()
        left = stack[-1]
        area = arr[top]*(right-left-1)
        maxarea = max(maxarea,area)
    return maxarea
#testing
nums = [2, 1, 5, 6, 2, 3]
print(max_area(nums))
