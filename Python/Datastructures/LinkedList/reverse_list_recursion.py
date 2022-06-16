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

    def reverse_list_recurse(self, pointer):
        if not pointer.next:      # if node is last it becomes head on reversing
            self.head = pointer
            return
        self.reverse_list_recurse(pointer.next)     # post recursion operation lead the processes starting from last
        temp = pointer.next
        temp.next = pointer    # next node is referenced to previous node
        # pointer.next = None    # current's next is broken so that it won't have two points

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
list.reverse_list_recurse(list.head)
list.print_list()
