class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        comb = []
        def backtrack(left, right):
            if left == right and left == n:
                res.append(''.join(comb))
                return

            if left < n:
                if left > right:
                    comb.append('(')
                    backtrack(left + 1, right)
                    comb.pop()
                    comb.append(')')
                    backtrack(left, right + 1)
                    comb.pop()
                else:
                    comb.append('(')
                    backtrack(left + 1, right)
                    comb.pop()
            else:
                comb.append(')')
                backtrack(left, right + 1)
                comb.pop()

        backtrack(0,0)
        return res