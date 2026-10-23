class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        comb = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(curDig):
            if len(comb) == len(digits):
                if not digits:
                    return
                res.append(''.join(comb))
                return
            
            for ch in digitToChar[digits[curDig]]:
                comb.append(ch)
                backtrack(curDig + 1)
                comb.pop()
        
        backtrack(0)
        return res