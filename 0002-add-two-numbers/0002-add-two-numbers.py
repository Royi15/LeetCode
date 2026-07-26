# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum=0
        carry = 1
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum +=  x*carry + y*carry   
            carry *=  10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        arr = [int(d) for d in str(sum)][::-1]
        head = None
        current = None
        for i in arr:
            new_node = ListNode(i)
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
        
        return head


        

        

        

        