class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.ref = None

    def add(self, data):
        temp = node(data)
        if not self.ref:
            self.ref = temp
            return
        current = self.ref
        while current.next:
            current = current.next
        current.next = temp

    def print_list(self):
        temp = self.ref
        if not temp:
            print()
            return
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()

def mergeLists(head1, head2):
    merged = linkedlist()
    while head1 and head2:
        if head1.val<head2.val:
            merged.add(head1.val)
            head1 = head1.next
        else:
            merged.add(head2.val)
            head2 = head2.next
    while head1:
        merged.add(head1.val)
        head1 = head1.next
    while head2:
        merged.add(head2.val)
        head2 = head2.next
    return merged



#testing
list1 = linkedlist()
list1.add(1)
list1.add(2)
list1.add(4)
list1.print_list()

list2 = linkedlist()
list2.add(1)
list2.add(3)
list2.add(4)
list2.print_list()

mergedList = mergeLists(list1.ref, list2.ref)
mergedList.print_list()
