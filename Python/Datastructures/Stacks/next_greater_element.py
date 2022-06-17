def next_greater(arr):
    stack = []
    stack.append(arr[-1])
    span = [-1 for i in range(len(arr))]
    for i in range(len(arr)-2, -1, -1):
        while stack and stack[-1] < arr[i]:
            stack.pop()
        span[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])
    return span

#testing
arr = [1, 3, 5, 2, 9, 8, 7]
print(next_greater(arr))

arr = [10, 3, 4, 2, 0, 5, 9, 8, 7, 11]
print(next_greater(arr))
