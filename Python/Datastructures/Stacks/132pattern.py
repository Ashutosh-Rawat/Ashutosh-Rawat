def pattern(nums):
    min_arr = []
    min_arr.append(arr[0])
    for i in range(1, len(nums)):
        min_arr.append(min(min_arr[i-1],nums[i]))

    stack = []
    for i in range(len(nums)):
        while stack and stack[-1]<min_arr[i]:
            stack.pop()
        if stack and stack[-1]<nums[i]:
            return True
        stack.append(nums[i])
    return False


# testing
arr = [3, 5, 0, 3, 4]
print(pattern(arr))

arr = [1, 2, 3, 4]
print(pattern(arr))


arr = [1, 3, 2, 4]
print(pattern(arr))

arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 23, 22]
print(pattern(arr))
