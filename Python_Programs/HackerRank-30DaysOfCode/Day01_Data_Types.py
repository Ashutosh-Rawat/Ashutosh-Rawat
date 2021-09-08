i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
second_i = 6    # declaring an int
second_d = 5.6  # declaring a float
second_s = "HackerRank is shit"    # declaring a string
# Read and save an integer, double, and String to your variables.
third_i = input()    # the input is a string even if you have entered an int or float
third_d = input()
third_s = input()
# Print the sum of both integer variables on a new line.
sum_i = i + int(third_i)      # third_i is a string so using type conversion to change it into int
print(sum_i)
# Print the sum of the double variables on a new line.
sum_d = d + float(third_d)
print(sum_d)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
sum_s = s + third_s
print(sum_s)

# test case:
# 12
# 4.0
# is the best place to learn and practice coding!
