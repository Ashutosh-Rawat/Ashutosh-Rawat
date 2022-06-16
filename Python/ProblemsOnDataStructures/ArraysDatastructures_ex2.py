print("Enter the number: ", end="")
number = int(input())
odd_list = []
for i in range(0, number+1):
    if i % 2 != 0:
        odd_list.append(i)
print(odd_list)