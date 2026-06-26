class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        cache = [[None] * (n + 1) for _ in range(n)]  # cache[i][j] for s[i:j]

        def is_palindrome(i: int, j: int) -> bool:  # j is exclusive
            if j - i <= 1:
                return True
            if cache[i][j] is not None:
                return cache[i][j]
            cache[i][j] = (s[i] == s[j - 1]) and is_palindrome(i + 1, j - 1)
            return cache[i][j]

        maxl = 1
        resi, resj = 0, 1

        for i in range(n):
            for j in range(i + 1, n + 1):
                p = cache[i][j]
                if p is None:              # not computed yet
                    p = is_palindrome(i, j)
                if p and (j - i) > maxl:   # <-- now using cached value
                    resi, resj = i, j
                    maxl = j - i

        return s[resi:resj]
