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
            return 
        current = head
        copy_dict = {}

        new_head = Node(current.val)
        copy_dict[current] = new_head
        current = current.next
        new_prev = new_head 

        while current:
            new = Node(current.val)
            copy_dict[current] = new
            new_prev.next = new
            new_prev = new
            current = current.next

        current = head 
        new_current = new_head
        while current:
            new_current.random = copy_dict.get(current.random,None)
            new_current = new_current.next
            current = current.next

        return new_head

        

        