# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        counterA = 0
        counterB = 0
        tempA=headA
        tempB=headB
        while tempA is not None:
            counterA+= 1
            tempA = tempA.next

        while tempB is not None:
            counterB+= 1
            tempB = tempB.next

        tempA=headA
        tempB=headB
        if counterA>counterB:
            for i in range(counterA-counterB):
                tempA = tempA.next
        elif counterB>counterA:
            for i in range(counterB-counterA):
                tempB = tempB.next

        while tempA is not None and tempB is not None:
            if tempA == tempB:
                return tempA

            tempA = tempA.next
            tempB = tempB.next
        
        return None



        