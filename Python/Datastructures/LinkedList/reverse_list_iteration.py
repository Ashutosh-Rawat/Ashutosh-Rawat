class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = node(data)
        if not self.head:
            self.head = temp
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = temp

    def print_list(self):
        temp = self.head
        print('list: ', end='')
        while temp:
            print(f' {temp.val} -> ', end='')
            temp = temp.next
        print('null')

    def reverse_list(self):
        current = self.head
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


#testing
list = linkedlist()
list.add(3)
list.add(4)
list.add(5)
list.add(6)
list.add(7)
list.add(8)
list.print_list()

#reversing list using iteration
list.reverse_list()
list.print_list()
