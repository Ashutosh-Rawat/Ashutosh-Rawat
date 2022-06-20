class queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [-1 for i in range(capacity)]
        self.front = self.rear = -1

    def enque(self,val):
        if self.front == -1:
            self.front = self.rear = 0
            self.arr[self.rear] = val
            return
        temp = (self.rear+1)%self.capacity
        if temp != self.front:
            self.rear = temp
        else:
            print('queue is full')
            return
        self.arr[self.rear] = val

    def deque(self):
        if self.front == -1:
            return 'queue is empty'
        temp = self.arr[self.front]
        self.arr[self.front] = -1
        if self.front == self.rear:
            self.rear = self.front = -1
            return temp
        if self.front == self.capacity-1:
            self.front = 0
            return temp
        self.front+=1
        return temp

    def print_queue(self):
        if self.front == -1:
            print('queue is empty')
            return
        if self.front == self.rear:
            print(self.arr[self.front])
            return
        i = self.front
        while True:
            print(self.arr[i], end=' ')
            i = (i+1)%self.capacity
            if i==self.rear:
                print(self.arr[i], end=' ')
                break
        print()

#testing
q = queue(3)
q.enque(3)   # queue : 3 -1 -1
q.enque(4)   # queue : 3  4 -1
q.enque(5)   # queue : 3  4  5
q.enque(6)   # queue is full
q.print_queue()

#dequeue
print('dequeue',q.deque())   # queue : -1 4 5
q.print_queue()

#enqueue
q.enque(7)    # queue : 7 4 5
q.print_queue()

print('dequeue',q.deque())     # queue : 7 -1 5
q.print_queue()

q.enque(8)    # queue : 7 8 5
print('dequeue',q.deque())     # queue : 7 8 -1
q.print_queue()

q.enque(9)    # queue : 7 8 9
q.print_queue()

#deque till empty
print('dequeue',q.deque())   # queue : -1 8 9
q.print_queue()
print('dequeue',q.deque())   # queue : -1 -1 9
q.print_queue()
print('dequeue',q.deque())   # queue : -1 -1 -1
q.print_queue()
print('dequeue',q.deque())
