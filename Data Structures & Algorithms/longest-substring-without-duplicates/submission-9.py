class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        count = {}
        l = 0 
        r = 0
        res = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            r += 1
            
            while count and count[s[r-1]] > 1:
                if s[l] in count:
                    count[s[l]] = count[s[l]] - 1
                    if count[s[l]] == 0:
                        del count[s[l]]
                l += 1
            res = max(res, r - l)

        return res