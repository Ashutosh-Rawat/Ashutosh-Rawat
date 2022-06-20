class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class queue:
    def __init__(self, capacity):
        self.front = self.rear = None
        self.capacity = capacity
        self.size = 0

    def enque(self,data):
        temp = node(data)
        if self.size == self.capacity:
            print('queue if full')
            return
        if not self.rear:
            self.front = self.rear = temp
            self.size+=1
            return
        self.rear.next = temp
        self.rear = temp
        self.size+=1

    def deque(self):
        if not self.front:
            return 'empty queue'
        temp = self.front.val
        self.size-=1
        self.front = self.front.next
        return temp

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        temp = self.front
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()

#testing
q = queue(3)
print(q.is_empty())
q.enque(3)
q.enque(4)
q.enque(5)
q.print_queue()
print(q.is_empty())
#queue is full
q.enque(10)

print(q.deque())
q.print_queue()

#emptying queue
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque)
