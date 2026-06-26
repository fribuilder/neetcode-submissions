# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head 
        while current:
            current = current.next
            length += 1

        if length == n:
            return head.next
        
        i_to_remove = length - n

        count = 0
        current = head
        while current:
            if count == i_to_remove - 1:
                current.next = current.next.next
                return head
            current = current.next
            count += 1