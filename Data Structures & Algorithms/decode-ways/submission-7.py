class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # dp[i] = number of ways to decode s[i:]
        dp = [0] * (n + 2)   # extra space so dp[i+2] is always safe
        dp[n] = 1            # empty suffix has 1 way

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue

            # take 1 digit
            dp[i] = dp[i + 1]

            # take 2 digits if valid (10..26)
            if i + 1 < n and int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]

            

             