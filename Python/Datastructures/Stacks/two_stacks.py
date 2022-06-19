class two_stack:
    def __init__(self,capacity):
        self.stack = [-1 for i in range(capacity)]
        self.top1 = -1
        self.top2 = capacity
        self.capacity = capacity

    def push1(self,num):
        if -1 not in self.stack:
            print('stack is full')
            return
        self.top1+=1
        self.stack[self.top1] = num

    def push2(self,num):
        if -1 not in self.stack:
            print('stack is full')
            return
        self.top2-=1
        self.stack[self.top2] = num

    def pop1(self):
        if self.top1 == -1:
            print('stack 1 is empty')
            return
        self.stack[self.top1] = -1
        self.top1-=1

    def pop2(self):
        if self.top2 == self.capacity:
            print('stack 2 is empty')
            return
        self.stack[self.top2] = -1
        self.top2+=1

    def peek1(self):
        if self.top1 == -1:
            print('stack 1 is empty')
            return
        return self.stack[self.top1]

    def peek2(self):
        if self.top2 == self.capacity:
            print('stack 2 is empty')
            return
        return self.stack[self.top2]


#testing
st = two_stack(5)
st.push1(2)
st.push1(3)

st.push2(10)
st.push2(11)
st.push2(13)
#pushing element in stack2 after stack is full
st.push2(15)
#pushing element in stack1 after stack is full
st.push1(1)
print('------------------------------------------------------')

print('stack 1 top: ', st.peek1())
print('stack 2 top: ', st.peek2())

#popping from first stack
st.pop1()
#popping form second stack
st.pop2()

print('stack 1 top: ', st.peek1())
print('stack 2 top: ', st.peek2())

#emptying the stacks
print('------------------------------------------------------')
st.pop1()
st.pop2()
st.pop1()
st.pop2()
st.pop2()
