def priority(op):
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    if op in prec.keys():
        return prec[op]
    else:
        return -1
def infix_to_prefix(string):
    operand = []
    operator = []
    for i in string:
        if i == ' ':
            pass
        elif i.isdigit() or i.isalpha():
            operand.append(i)
        elif i == '(':
            operator.append(i)
        elif i in ')':
            while operator and operator[-1]!='(':
                opn1 = operand.pop()
                opn2 = operand.pop()
                op = operator.pop()
                operand.append(op+opn2+opn1)
            operator.pop()   # popping opening brackets
        else:
            while operator and priority(i) <= priority(operator[-1]):
                opn1 = operand.pop()
                opn2 = operand.pop()
                op = operator.pop()
                operand.append(op+opn2+opn1)
            operator.append(i)
    while operator:
        if operator[-1] == '(':
            return 'invalid expression'
        opn1 = operand.pop()
        opn2 = operand.pop()
        op = operator.pop()
        operand.append(op+opn2+opn1)

    return operand[-1]


#testing
string = 'a * b + c / d'
print(infix_to_prefix(string))

string = 'a * ( b + c ) / d'
print(infix_to_prefix(string))

string = 'a+2*3'
print(infix_to_prefix(string))

string = 'a*2+3'
print(infix_to_prefix(string))

string = 'a*2/3+0'
print(infix_to_prefix(string))
string = 'a+(b+c/d)+e*f'
print(infix_to_prefix(string))

string = '2*3+0/4*2+(2*3)+2*(2*4)'
print(infix_to_prefix(string))

string = '3 * 2 * 2 ( 2 + 0'
print(infix_to_prefix(string))
