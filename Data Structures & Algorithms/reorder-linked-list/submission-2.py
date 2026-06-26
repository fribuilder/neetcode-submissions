# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        head1 = head
        count = 0
        current = head
        while current:
            current = current.next 
            count += 1
        index = count
        half = count // 2
        
        count = 0
        current = head
        while current:
            if count < half:
                current = current.next
            if count == half:
                new = current.next
                current.next = None
                prev = None
                current = new
            if count > half:
                new_list = current.next
                current.next = prev
                if count == index - 1:
                    head2 = current
                prev = current
                current = new_list
            count += 1
        
        count = 0
        first, second = head1, head2
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
 


        

        

