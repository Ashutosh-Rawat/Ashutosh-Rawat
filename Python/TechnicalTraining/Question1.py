array = [10, 5, 0, 8, 0, 9, 0, 0, 2, 0]
print(array)
for i in range(len(array)):
    if array[i] == 0:
        for j in range(i+1, len(array)):
            if array[j] != 0:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    else:
        continue

print(array)

