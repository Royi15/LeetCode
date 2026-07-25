# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        counter = 0
        temp = head
        while temp is not None:
            counter += 1
            temp = temp.next

        if n == counter:
            return head.next

        temp = head
        for i in range(counter - n - 1):
            temp = temp.next

        temp.next = temp.next.next
        return head
        