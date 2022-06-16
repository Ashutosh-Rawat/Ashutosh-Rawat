# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_no(key, dictionary):
    if key in dictionary:
        phone_number = phonebook[key]
        print(key + "=" + str(phone_number))
    else:
        print("Not found")


phonebook = {}
number = input()
for i in range(int(number)):
    entry = input()
    name, phone_no = entry.split()
    phonebook[name] = phone_no

itr = 0
input_name = input()
while itr == 0 or input_name is not None:
    get_no(input_name, phonebook)
    input_name = None
    itr += 1

# input example1
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry

