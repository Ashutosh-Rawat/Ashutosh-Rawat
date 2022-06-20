class queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.arr = [-1 for i in range(self.capacity)]
        self.front = self.rear = 0

    def enqueue(self, val):
        if self.rear == self.capacity:
            print('queue is full')
            return
        available_index = (self.front+self.rear)% self.capacity
        self.arr[available_index] = val
        self.rear+=1

    def is_empty(self):
        return self.rear == 0

    def dequeue(self):
        if self.rear == 0:
            return 'queue is empty'
        value = self.arr[self.front]
        self.arr[self.front] = -1
        self.front = (self.front+1)% self.capacity
        self.rear-=1
        return value

    def print_queue(self):
        for i in range(self.rear):
            available_index = (self.front+i)% self.capacity
            print(self.arr[available_index], end=' ')
        print()

#testing
q = queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print_queue()

#dequeue
print('dequeue: ',q.dequeue())
q.print_queue()

#dequeue
print('dequeue: ',q.dequeue())
q.print_queue()

print('dequeue: ',q.dequeue())
q.print_queue()
print('dequeue: ',q.dequeue())

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.print_queue()
q.enqueue(8)
q.print_queue()
q.dequeue()
q.enqueue(9)
q.print_queue()
q.enqueue(1)
q.print_queue()
q.dequeue()
q.print_queue()
q.enqueue(2)
q.print_queue()
