from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'[':']','{':'}','(':')'}
        queue = deque()
        for ch in s:
            if queue and queue[-1] in ['}',']',')']:
                return False
            if queue and mapping[queue[-1]] == ch:
                queue.pop()
            else:
                queue.append(ch)
        
        return True if not queue else False


            

            
