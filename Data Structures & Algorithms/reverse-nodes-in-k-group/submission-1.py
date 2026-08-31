# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        group = 0
        while group < k and curr:
            curr = curr.next
            group += 1

        if group == k:
            curr = head
            prev = None
            while group > 0:
                new = curr.next
                curr.next = prev
                prev = curr
                curr = new
                group -= 1
            head.next = self.reverseKGroup(new, k)
            return prev
        else:
            return head
