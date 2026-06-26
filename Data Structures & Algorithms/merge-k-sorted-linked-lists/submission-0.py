# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        not_empty = False
        for i, current in enumerate(lists):
            if current.val != None:
                not_empty = True

        if not not_empty:
            return None 

        dummy = ListNode(None)
        prev_min = dummy 
        while not_empty:
            min_value = 1e10
            min_idx = -1
            for i, current in enumerate(lists):
                if current == None:
                    continue
                elif current.val < min_value:
                    min_value = current.val
                    min_idx = i
                else: continue
            
            if min_value == 1e10:
                not_empty = False
                continue 

            prev_min.next = lists[min_idx]
            prev_min = prev_min.next 
            lists[min_idx] = lists[min_idx].next

        return dummy.next


        