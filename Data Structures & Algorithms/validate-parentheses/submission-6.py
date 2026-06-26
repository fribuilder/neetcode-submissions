from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        tube =  deque()
        left = ['(','[','{']
        right = [')',']','}']
        match = dict(zip(left,right))

        for ch in s:
            if ch in left:
                tube.append(ch)
            else:
                if not tube or match[tube[-1]] != ch:
                    return False
                else:
                    tube.pop()

        return not tube 


            

            
