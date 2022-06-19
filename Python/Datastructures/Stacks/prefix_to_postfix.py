def precedence(ch):
    operators = {'+':1, '-':1, '*':2, '/':2, '^':3}
    if ch in operators.keys():
        return operators[ch]

def prefix_to_postfix(string):
    operator = []
    operand = []
    for i in string[::-1]:
        if i == ' ':
            pass
        elif i.isalpha() or i.isdigit():
            operand.append(i)
        else:
            operator.append(i)
            while operator and precedence(i) <= precedence(operator[-1]):
                opn2 = operand.pop()
                opn1 = operand.pop()
                op = operator.pop()
                operand.append(opn2+opn1+op)
    while operator:
        opn2 = operand.pop()
        opn1 = operand.pop()
        op = operator.pop()
        operand.append(opn2+opn1+op)
    return operand[-1]

def pre_to_post(string):    # this method is more acceptable as it has the same logic as that but less time complexity
    stack = []
    for i in string[::-1]:
        if i == ' ':
            pass
        elif i.isdigit() or i.isalpha():
            stack.append(i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1+op2+i)
    return stack[-1]
#testing
print('direct method')
string = '+*ab/cd'
print(pre_to_post(string))
string = '/*a+bcd'
print(pre_to_post(string))

print('\nself methods')
string = '+*ab/cd'
print(prefix_to_postfix(string))
string = '+a*23'
print(prefix_to_postfix(string))
string = '+*a23'
print(prefix_to_postfix(string))
string = '+/*a230'
print(prefix_to_postfix(string))
string = '++a+b/cd*ef'
print(prefix_to_postfix(string))
string = '+++*23*/042*23*2*24'
print(prefix_to_postfix(string))
