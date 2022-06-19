def postfix_to_prefix(arr):
    stack = []
    for i in arr:
        if i == ' ':
            pass
        elif i.isdigit() or i.isalpha():
            stack.append(i)
        else:
            opn1 = stack.pop()
            opn2 = stack.pop()
            stack.append(i+opn2+opn1)
    return stack[-1]

#testing
# direct method
string = 'ab*cd/+'
print(postfix_to_prefix(string))
string = 'abc+*d/'
print(postfix_to_prefix(string))

# self methods
string = 'ab*cd/+'
print(postfix_to_prefix(string))
string = 'a23*+'
print(postfix_to_prefix(string))
string = 'a2*3+'
print(postfix_to_prefix(string))
string = 'a2*3/0+'
print(postfix_to_prefix(string))
string = 'abcd/++ef*+'
print(postfix_to_prefix(string))
string = '23*04/2*+23*+224**+'
print(postfix_to_prefix(string))
