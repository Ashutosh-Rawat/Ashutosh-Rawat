def previous_greater(arr):
    stack = []
    stack.append(arr[0])
    span = [-1 for i in range(len(arr))]

    for i in range(1,len(arr)):
        while stack and stack[-1] < arr[i]:
            stack.pop()

        span[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])
    return span

# testing
arr = [2, 3, 5, 1, 0, 2, 10, 5, 3, 12, 13, 9]
span = previous_greater(arr)
print(span)

arr = [1, 3, 5, 7, 9]
span = previous_greater(arr)
print(span)

arr = [9, 7, 5, 3, 1]
span = previous_greater(arr)
print(span)
