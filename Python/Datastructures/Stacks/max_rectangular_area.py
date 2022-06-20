def max_area(nums):
    result = 0
    for i in range(len(nums)):
        current = nums[i]
        for j in range(i-1,-1,-1):
            if nums[j]>=nums[i]:
                current+=nums[i]
            else:
                break
        for j in range(i+1,len(nums)):
            if nums[j]>=nums[i]:
                current+=nums[i]
            else:
                break
        result = max(current, result)
    return result


#testing
nums = [2, 1, 5, 6, 2, 3]
print(max_area(nums))
