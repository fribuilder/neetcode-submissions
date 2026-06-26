class Solution:
    def partition(self, s: str) -> List[List[str]]:
        split = []
        res = []

        def backtrack(i):
            if i >= len(s):
                if check_palindrome(split[-1]):
                    res.append(split.copy())
                    return 
                return 
            
            if split:
                split[-1] += s[i]
                backtrack(i+1)
                split[-1] = split[-1][:-1]

                if check_palindrome(split[-1]):
                    split.append(s[i])
                    backtrack(i+1)
                    split.pop()
            else:
                split.append(s[i])
                backtrack(i+1)

        def check_palindrome(s):
            if not s:
                return True
            else:
                return s[::-1] == s

        backtrack(0)
        return res