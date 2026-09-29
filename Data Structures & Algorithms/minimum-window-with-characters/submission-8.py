class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        count = {}
        ele = 0
        min_len = float('inf')
        
        for i in range(len(t)):
            count[t[i]] = count.get(t[i],0) + 1
        
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    ele += 1

            while ele == len(count):
                if r - l + 1 < min_len:
                    min_len = min(min_len, r-l+1)
                    res = s[l:r+1]

                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] == 1:
                        ele -= 1
                
                l += 1
            

        return res if min_len < float('inf') else ''
             
