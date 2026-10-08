"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}
        cur = head
        prev = Node(0)
        while cur:
            new = Node(cur.val)
            old_to_new[cur] = new
            prev.next = new
            cur = cur.next
            prev = new
        
        cur = head
        while cur:
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            else:
                old_to_new[cur].random = None
            cur = cur.next
        
        return old_to_new[head]
        


