def check_balance(string):
    if len(string)<=1:
        return False
    map = {'(':')', '{':'}', '[':']'}
    stack = []
    index = -1
    for i in string:
        if i in map.values():
            if index == -1:
                return False
            if i == map[stack[index]]:
                stack.pop()
                index-=1
            else:
                return False
        if i in map.keys():
            stack.append(i)
            index+=1
    return index == -1


#testing
string = '[ 1 + ( 2 * 3 ) ]'
print(check_balance(string))

string = '[ ( 2 + 3 + 4 / 4 { } [ 6 ] 4 ] '
print(check_balance(string))

string = '{ 2 + { 3 - ( 4 * 5 ) } } \ ]'
print(check_balance(string))

string = '{ 2 * 3 - [ 4 + 6 ] { 4 } ( ) { } / 2 * 4 }'
print(check_balance(string))

string = '{ 2 * 4 + [ 2 * 4 ] ( 5 ) % 2 { 2 * 6 } / { 2 - 5 } * ( 5 ) }'
print(check_balance(string))
