class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        length = 1
        set_s = [s[left:right]]
        if not s:
            return 0
        while right < len(s):
            if s[right] in set_s:
                left += 1
                set_s.pop(0)
            else:
                length = max(length, right - left + 1)
                set_s.append(s[right])
                right += 1
        return length


        