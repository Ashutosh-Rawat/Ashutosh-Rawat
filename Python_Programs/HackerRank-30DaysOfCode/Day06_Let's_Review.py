# Enter your code here. Read input from STDIN. Print output to STDOUT
no_test_case = input()

for i in range(int(no_test_case)):     # i represents every number from 0 to no_test_case-1
    case = input()
    odd_index = ""
    even_index = ""
    for j in range(len(case)):
        if j % 2 == 0:      # % is modulus which gives remainder j divided by 2 , good for even number checking
            even_index += case[j]  # += means adding even_index to case[j] first and then adding it to even_index
        else:
            odd_index += case[j]
    print(even_index, odd_index)

# 2
# Hacker
# Rank
