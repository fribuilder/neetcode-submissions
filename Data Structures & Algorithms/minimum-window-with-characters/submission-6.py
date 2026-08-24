class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = count.get(ch, 0) + 1
        missing = len(t)                      # 还差多少个字符

        right = 0
        res = ''
        min_len = len(s) + 1
        for left in range(len(s)):
            while missing > 0 and right < len(s):
                if s[right] in count:
                    if count[s[right]] > 0:   # 只有正数才算"补上了一个缺口"
                        missing -= 1
                    count[s[right]] -= 1
                right += 1

            length = right - left
            if missing == 0 and length < min_len:
                res = s[left:right]
                min_len = length

            if s[left] in count:
                count[s[left]] += 1
                if count[s[left]] > 0:        # 回收后又变成缺口
                    missing += 1

        return res