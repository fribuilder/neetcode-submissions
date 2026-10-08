# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0
        dummy = ListNode(None)
        prev = dummy

        while l1 or l2 or add != 0 :
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            new_val = (val1 + val2 + add) % 10
            print(add, new_val)
            new_node = ListNode(new_val)
            
            add = (val1 + val2 + add) // 10
            prev.next = new_node
            prev = new_node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next