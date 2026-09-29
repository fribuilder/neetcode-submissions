class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        dist = 0
        length = 0
        for r in range(0,len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while r - l - max(count.values()) + 1 > k:
                count[s[l]] -= 1
                l += 1
            length = max(length, r-l+1)
        return length