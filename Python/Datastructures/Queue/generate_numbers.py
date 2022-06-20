class queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.rear = self.front = -1
        self.queue = []

    def enqueue(self,val):
        if self.rear == self.capacity-1:
            print('queue is full')
            return
        if self.front==-1:
            self.front+=1
        self.rear+=1
        self.queue.append(val)

    def dequeue(self):
        if self.front == -1:
            return 'queue is empty'
        if len(self.queue)==1:
            self.front = self.rear = -1
        self.rear-=1
        return self.queue.pop(0)

    def print_queue(self):
        current = self.front
        while current!=len(self.queue):
            print(self.queue[current],end = ' ')
            current+=1
        print()

    def is_empty(self):
        return self.front==-1


def generate_numbers(num, arr):
    nums = []
    if num<=2:
        return arr
    qu = queue(2*num)
    for i in arr:
        qu.enqueue(str(i))
    while num>0:
        temp = qu.dequeue()
        nums.append(temp)
        qu.enqueue(temp+'5')
        qu.enqueue(temp+'6')
        num-=1
    print(nums)

#testing
num = 10
arr = [5, 6]
generate_numbers(num,arr)
