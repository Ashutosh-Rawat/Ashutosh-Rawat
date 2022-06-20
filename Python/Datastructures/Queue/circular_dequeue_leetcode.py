class deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [-1 for i in range(capacity)]
        self.front = self.rear = -1

    def insert_front(self,val):
        if self.front == -1:
            self.front = self.rear = 0
            self.arr[self.rear] = val
            return
        temp = (self.front-1)%self.capacity
        if temp != self.rear:
            self.front = temp
        else:
            print('queue is full')
            return
        self.arr[self.front] = val

    def insert_rear(self,val):
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

    def delete_front(self):
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

    def delete_rear(self):
        if self.rear == -1:
            return 'queue is empty'
        temp = self.arr[self.rear]
        self.arr[self.rear] = -1
        if self.rear == self.front:
            self.rear = self.front = -1
            return temp
        if self.rear == 0:
            self.rear = self.capacity-1
            return temp
        self.rear-=1
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
q = deque(3)
q.insert_front(1)
q.insert_rear(2)
q.insert_front(0)
q.print_queue()

#delete front
print('front dequeue: ',q.delete_front())
q.print_queue()

#delete rear
print('rear dequeue: ',q.delete_rear())
q.print_queue()

q2 = deque(3)
q2.insert_rear(1)
q2.insert_rear(2)
q2.insert_rear(3)
q2.print_queue()
