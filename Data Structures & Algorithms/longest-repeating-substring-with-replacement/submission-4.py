class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        maxc = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxc = max(maxc, count[s[r]])
            if r - l + 1 - maxc > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            res = max(r - l + 1, res)
        
        return res