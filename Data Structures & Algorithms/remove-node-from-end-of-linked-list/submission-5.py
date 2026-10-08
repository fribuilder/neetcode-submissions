# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        dummy = ListNode(None)
        dummy.next = head
        slow, fast = dummy, dummy
        idx = 0
        while fast:
            if idx <= n:
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
            idx += 1

        print(slow.val)
        slow.next = slow.next.next

        return dummy.next
        
        
