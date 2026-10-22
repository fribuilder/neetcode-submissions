class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        comb = []

        def backtrack(s):
            if s == '':
                res.append(comb.copy())
                return
            
            for i in range(len(s)):
                if ispal(s[:i+1]):
                    comb.append(s[:i+1])
                    backtrack(s[i+1:])
                    comb.pop()

        def ispal(s):
            if s == s[::-1]:
                return True
        
        backtrack(s)
        return res