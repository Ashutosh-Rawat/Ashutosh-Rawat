def next_smaller(arr):
    stack = []
    stack.append(arr[-1])
    span = [-1 for i in range(len(arr))]
    for i in range(len(arr)-2, -1, -1):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        span[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])
    return span

#testing
arr = [1, 3, 10, 4, 8, 5, 9, 8, 6, 2, 1]
print(next_smaller(arr))
