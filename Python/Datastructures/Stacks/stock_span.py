def get_span(arr):
    if not arr:
        return None
    stack = []
    stack.append(0)
    span = [1 for i in range(len(arr))]
    for i in range(1,len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        span[i] = i+1 if not stack else i-stack[-1]
        stack.append(i)
    return span

arr = [1, 3, 2, 10, 2, 3, 8, 5, 7, 11, 9]
span = get_span(arr)
print(span)

arr = []
print(get_span(arr))
