class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class linkedlist:
    def __init__(self):
        self.ref = None

    def add(self, data):
        temp = ListNode(data)
        if not self.ref:
            self.ref = temp
            return
        current = self.ref
        while current.next:
            current = current.next
        current.next = temp

    def print_list(self):
        temp = self.ref
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()


class Solution():
    def __init__(self):
        self.head = None
    def mergeTwoLists(self, list1, list2):
        list = ListNode()
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

    def print_merge(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()

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

merged = Solution()
merged.mergeTwoLists(list1.ref, list2.ref)
merged.print_merge()