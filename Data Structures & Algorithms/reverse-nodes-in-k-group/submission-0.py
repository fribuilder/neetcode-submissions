# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        new_head = head
        current_head = head
        section = 1
        prev_tail = current_head
        while current_head:
            len_check = current_head
            for i in range(k-1):
                if len_check.next == None:
                    return new_head
                len_check = len_check.next

            current = current_head.next
            prev = current_head
            count = 1
            while count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1
            
            if section == 1:
                new_head = prev
            if section > 1: 
                prev_tail.next = prev 
                prev_tail = current_head
                
            current_head.next = current
            current_head = current

            section += 1
        
        return new_head
            



            

                
            
                
        