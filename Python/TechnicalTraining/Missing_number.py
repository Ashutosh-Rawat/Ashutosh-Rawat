array = [1, 3, 4, 5, 6, 7, 8]
n = array[-1]
natural_sum = int(n*(n+1)/2)
sum_num = 0

for i in array:
    sum_num = sum_num + i

print("Missing num: ", natural_sum-sum_num)
