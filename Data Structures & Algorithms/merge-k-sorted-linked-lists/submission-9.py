# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        pairs = [(head.val, i) for i, head in enumerate(lists) if head]
        heapq.heapify(pairs)
        dummy = ListNode()

        cur = dummy 
        while pairs:
            min_pair = heapq.heappop(pairs)
            cur.next = lists[min_pair[1]]
            if lists[min_pair[1]].next:
                heapq.heappush(pairs, (lists[min_pair[1]].next.val, min_pair[1]))
            cur = lists[min_pair[1]]
            lists[min_pair[1]] = lists[min_pair[1]].next

        return dummy.next

