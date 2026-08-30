# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        curr = mid

        def flip(head: Optional[ListNode]):
            curr = head
            if not curr or not curr.next:
                return curr
            new_head = flip(head.next)
            curr.next.next = curr
            curr.next = None
            return new_head

        half_head = flip(mid)
        
        def print_out(head):
            curr = head
            while curr:
                print(curr.val)
                curr = curr.next
                
        print_out(half_head)

        def merge(head1, head2):
            if not head1:
                return head2
            elif not head2:
                return head1
            if (not head1) and (not head2):
                return None
            
            new_head1 = head1.next
            new_head2 = head2.next
            head1.next = head2
            head2.next = merge(new_head1, new_head2)

            return head1
        
        merge(head, half_head)




        