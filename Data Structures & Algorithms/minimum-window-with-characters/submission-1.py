class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i],0) + 1
        
        left, right = 0, 0
        length = len(s) + 1
        while left < len(s):
            while max(count_t.values()) > 0 and right < len(s):
                if s[right] in t:
                    count_t[s[right]] -= 1
                right = right + 1
                print(f'{count_t}, left: {left}, right: {right}')
            if max(count_t.values()) == 0 and right - left + 1 <= length:
                length = right - left
                res = s[left: right]

            if s[left] in t:
                count_t[s[left]] += 1
                        
            left += 1
        
        return res if length <= len(s) else '' 
