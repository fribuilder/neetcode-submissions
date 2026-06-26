class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str,int] = {}
        start = 0
        max_length = 0

        for end, ch in enumerate(s):
            # 1) If we've seen ch inside the current window, jump start
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch] + 1

            # 2) Record/update the last-seen position of ch
            last_seen[ch] = end

            # 3) Update max_length for the window s[start..end]
            max_length = max(max_length, end - start + 1)

        return max_length


        