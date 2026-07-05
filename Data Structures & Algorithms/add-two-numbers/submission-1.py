# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = dummy = ListNode()
        count = 0
        print(18 % 10)
        while l1 or l2 or (count != 0):
            val_l1 = int(l1.val) if l1 else 0
            val_l2 = int(l2.val) if l2 else 0
            num = (val_l1 + val_l2 + count) % 10
            count = (val_l1 + val_l2 + count) // 10

            new_head = ListNode(num)
            pre_head.next = new_head
            pre_head = new_head
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next