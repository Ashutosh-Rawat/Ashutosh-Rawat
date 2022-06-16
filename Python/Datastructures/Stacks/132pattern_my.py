def pattern(nums):
    minv = nums[0]
    stack = []
    for i in range(1, len(nums)):
        while stack and nums[i]>stack[-1]:
            stack.pop()
        if stack and nums[i]<stack[-1] and stack[-1] is not minv:
            return True
        stack.append(nums[i])
        minv = min(nums[i], minv)
    return False

#testing
arr = [3, 5, 0, 3, 4]
print(pattern(arr))

arr = [1, 2, 3, 4]
print(pattern(arr))


arr = [1, 3, 2, 4]
print(pattern(arr))

arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 23, 22]
print(pattern(arr))
