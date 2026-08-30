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
        dummy = Node(-1)
        prev = dummy
        curr = head
        table = {}
        while curr:
            new = Node(curr.val)
            table[curr] = new
            prev.next = new
            prev = new
            curr = curr.next

        # curr = dummy.next
        # while curr:
        #     print(curr.val)
        #     print(curr.random.val) if curr.random else print('None')
        #     curr = curr.next

        curr_old = head
        curr_new = dummy.next
        while curr_new:
            if curr_old.random:
                curr_new.random = table[curr_old.random]
            curr_new = curr_new.next
            curr_old = curr_old.next

        return dummy.next 
        