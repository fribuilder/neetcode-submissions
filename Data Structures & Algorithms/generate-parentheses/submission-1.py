class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        paren = []

        def backtrack(i, count_a, count_b):
            if i >= 2 * n:
                if count_a == count_b:
                    res.append(''.join(paren))
                return
            if count_a < count_b:
                return
            
            paren.append('(')
            backtrack(i+1, count_a + 1, count_b)
            paren.pop()
            paren.append(')')
            backtrack(i+1, count_a, count_b + 1)
            paren.pop()
        
        backtrack(0,0,0)
        return res