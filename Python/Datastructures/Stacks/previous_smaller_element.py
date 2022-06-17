def previous_smaller(arr):
    stack = []
    stack.append(arr[0])
    span = [-1 for i in range(len(arr))]
    for i in range(1,len(arr)):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        span[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])
    return span

#testing
arr = [1, 3, 10, 2, 12, 5, 7, 9, 3, 0]
print(previous_smaller(arr))
