class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev, cur = None, mid.next
        slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev= cur
            cur = next_node
        
        new_start = prev
        start1 = head
        while new_start and start1:
            h1, h2 = start1.next, new_start.next
            start1.next = new_start
            new_start.next = h1
            new_start, start1 = h2, h1


