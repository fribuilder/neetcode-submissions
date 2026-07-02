# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur_head = head
        last_head = None
        while cur_head:
            next_head = cur_head.next
            if not last_head:
                cur_head.next = None
            else:
                cur_head.next = last_head
            last_head = cur_head
            cur_head = next_head

        return last_head
