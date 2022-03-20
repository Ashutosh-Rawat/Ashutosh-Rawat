# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_no(name, dictionary):
    if name in dictionary:
        phone_number = phonebook[name]
        print(name + "=" + str(phone_number))
    else:
        print("Not found")


phonebook = {}     # initializing and empty dictionary
number = input()
for i in range(int(number)):
    entry = input()
    name, phone_no = entry.split()    # split() splits two or more inputs according to punctuation between them
    phonebook[name] = phone_no

input_name = input()
while input_name:
    try:    # try has the error block and except is used to ignore mentioned error in the block
        get_no(input_name, phonebook)
        input_name = input()
    except EOFError:     # this is to get rid of End of File error , check online
        break     # break when encountered, then a loop is terminated

# sample input:

# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry




