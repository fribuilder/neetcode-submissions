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
            
        cur = head
        oldtocopy = {}
        pre_node = None 

        while cur:
            oldtocopy[cur] = Node(cur.val)
            if pre_node:
                pre_node.next = oldtocopy[cur]
            pre_node = oldtocopy[cur]
            cur = cur.next

        pre_node.next = None
        oldtocopy[cur] = None

        cur = head
        while cur:
            oldtocopy[cur].random = oldtocopy[cur.random]
            cur = cur.next

        return oldtocopy[head]