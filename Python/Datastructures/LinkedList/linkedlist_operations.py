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

    def add_at_beg(self, data):
        temp = node(data)
        if not self.head:
            self.head = temp
            return
        temp.next = self.head
        self.head = temp

    def add_at_pos(self, data, pos):
        temp = node(data)
        if not self.head:
            self.head = temp
            return
        current = self.head
        prev = None
        while pos>0:
            if not current:
                print('position greater than size of list')
                return
            prev = current
            current = current.next
            pos-=1
        prev.next = temp
        temp.next = current

    def print_list(self):
        temp = self.head
        print('list: ', end='')
        while temp:
            print(f' {temp.val} -> ', end='')
            temp = temp.next
        print('null')

    def delete_at_beg(self):
        self.head = self.head.next

    def delete_at_last(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_n(self, pos):
        current = self.head
        prev = None
        while pos>0:
            if not current:
                print('position greater than size of list')
                return
            prev = current
            current = current.next
            pos-=1
        prev.next = current.next

#testing
list = linkedlist()
list.add(3)
list.add(4)
list.add(5)
list.print_list()
# adding at beginning
list.add_at_beg(1)
list.add_at_beg(10)
list.print_list()
# adding the nth position
list.add_at_pos(11, 3)   # working perfectly
list.print_list()

#deleting from beginning
list.delete_at_beg()
list.print_list()

#deleting from last
list.delete_at_last()
list.print_list()

#deleting at nth position
list.delete_at_n(3)
list.print_list()

list.add(4)
list.add(5)
list.add(6)
list.print_list()
list.delete_at_n(2)
list.print_list()
