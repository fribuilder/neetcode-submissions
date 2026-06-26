class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        init_idx = 0
        '''What we know: dp[i][j] depends on the value of dp[i+1][j-1], therefore the
        iteration should goes deceasing for i and goes increasing for j'''
        for i in range(n-1,-1,-1): 
            dp[i][i] = True
            if i < n-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                if max_len < 2:
                    max_len = 2
                    init_idx = i
            
            if i+2 < n: #exclude idx out of bound case
                for j in range(i+2,n):
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                    if dp[i][j] and max_len < (j - i + 1):
                        max_len = j - i + 1
                        init_idx = i

        return s[init_idx : init_idx + max_len]


                





            

