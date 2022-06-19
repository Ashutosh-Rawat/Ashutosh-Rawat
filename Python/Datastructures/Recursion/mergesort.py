def mergesort(arr):
    if len(arr) <= 1:
        return arr
    l1 = mergesort(arr[:len(arr)//2])
    l2 = mergesort(arr[len(arr)//2:])
    return merge(l1,l2)

def merge(arr1, arr2):
    merged_arr = []
    while arr1 and arr2:
        if arr1[0]>arr2[0]:
            merged_arr.append(arr2[0])
            arr2.pop(0)
        else:
            merged_arr.append(arr1[0])
            arr1.pop(0)
    while arr1:
        merged_arr.append(arr1[0])
        arr1.pop(0)
    while arr2:
        merged_arr.append(arr2[0])
        arr2.pop(0)
    return merged_arr


#testing
arr = [1, 3, 2, 5, 4]
print(mergesort(arr))

arr = [1, 3, 6, 0, 2, 3, 1, 9, 11, 2, 8, 9, 4]
sorted = mergesort(arr)
print(sorted)

arr = [i for i in range(15,-1,-1)]
print(mergesort(arr))
