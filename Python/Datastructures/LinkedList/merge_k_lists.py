class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution():
    def __init__(self):
        self.head = None
    def mergeTwoLists(self, list1, list2):
        list = node()
        head= list
        while list1 and list2:
            if list1.val>list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        self.head = list.next     # should not be added in leetcode
        return list.next

    def mergeKLists(self, lists):
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged
        self.head = lists[0]      # not to be added in leetcode
        return lists[0]

    def print_list_m(self):
        temp = self.head
        print('\nlist: ', end=' ')
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print('\n')

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

list3 = linkedlist()
list3.add(1)
list3.add(5)
list3.add(6)
list3.add(8)
list3.print_list()

list4 = linkedlist()
list4.add(7)
list4.add(8)
list4.add(9)
list4.add(10)
list4.print_list()

list5 = linkedlist()
list5.add(10)
list5.add(11)
list5.print_list()

arr = [list1.ref, list2.ref, list3.ref, list4.ref, list5.ref]
list = Solution()
list.mergeKLists(arr)
list.print_list_m()
