# Definition for singly-linked list.
import sys
sys.setrecursionlimit(10**5)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    import heapq

    def mergeKLists(self, lists):
        heap = [(h.val, i, h) for i, h in enumerate(lists) if h]
        heapq.heapify(heap)
        dummy = cur = ListNode()
        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next

        