class queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.front = self.rear = -1
        self.stack = []

    def enqueue(self,val):
        if self.rear == self.capacity-1:
            print('queue is full')
            return
        if self.front == -1:
            self.front+=1
        self.rear+=1
        self.stack.append(val)

    def dequeue(self):
        if self.rear == -1:
            return 'queue is empty'
        arr = []
        while self.stack:
            arr.append(self.stack.pop())
        temp = arr.pop()
        while arr:
            self.stack.append(arr.pop())
        if not self.stack:
            self.rear = self.front = -1
            return temp
        self.rear-=1
        return temp

    def print_queue(self):
        arr = []
        while self.stack:
            arr.append(self.stack.pop())
        while arr:
            temp = arr.pop()
            print(temp,end=' ')
            self.stack.append(temp)
        print()

    def is_empty(self):
        return self.front == -1

#testing
q = queue(3)
print(q.is_empty())
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print_queue()

# is queue empty
print(q.is_empty())
#queue is full
q.enqueue(10)

print('dequeue: ',q.dequeue())
q.print_queue()

#emptying queue
print('dequeue: ',q.dequeue())
print('dequeue: ',q.dequeue())
print('dequeue: ',q.dequeue())
print(q.dequeue)
