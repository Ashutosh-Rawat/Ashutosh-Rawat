def precedence(op):
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    if op in prec.keys():
        return prec[op]
    else:
        return -1

def infix_to_postfix(string):
    result = ''
    stack = []
    for i in string:
        if i.isdigit() or i.isalpha():      # if the current iteration is alphabet or digit
            result+=i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':    # while the digits in brackets (higher precedence) is not solved first
                result += stack.pop()    # pop the output from the stack until next '(' is encountered
            if stack and stack[-1] != '(':    # if the current digit is openining bracket and there is not close bracket
                return 'invalid expression'
            else:
                stack.pop()
        elif i == ' ':   # if the expression contains any whitespace, ignore it
            pass
        else:     # is the current iteration is an operator
            while stack and precedence(i) <= precedence(stack[-1]):
                if stack[-1] == '(':
                    return 'invalid expression'
                result+=stack.pop()
            stack.append(i)
    while stack:
        if stack[-1] == '(':
            return 'invalid expression'
        result+=stack.pop()
    return result

#testing
string = 'a * b + c / d'
print(infix_to_postfix(string))

string = 'a * ( b + c ) / d'
print(infix_to_postfix(string))

string = 'a+2*3'
print(infix_to_postfix(string))

string = 'a*2+3'
print(infix_to_postfix(string))

string = 'a*2/3+0'
print(infix_to_postfix(string))
string = 'a+(b+c/d)+e*f'
print(infix_to_postfix(string))

string = '2*3+0/4*2+(2*3)+2*(2*4)'
print(infix_to_postfix(string))

string = '3 * 2 * 2 ( 2 + 0'
print(infix_to_postfix(string))
