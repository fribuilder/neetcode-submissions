# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_int = 0
        prev_int = 0
        dummy = ListNode(0)
        prev_list = dummy
        while l1 or l2 or prev_int != 0:
            if not l1:
                int1 = 0
            else:
                int1 = l1.val
            
            if not l2:
                int2 = 0 
            else:
                int2 = l2.val 

            if int1 + int2 + prev_int> 9:
                next_int = 1
            next_list = ListNode((int1 + int2 + prev_int) % 10)
            prev_list.next = next_list

            prev_list = next_list
            prev_int = next_int
            next_int = 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


