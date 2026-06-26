class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for i in s:
            if not(i in dic_s.keys()):
                dic_s[i] = 1
            else: dic_s[i] += 1

        dic_t = {}
        for i in t:
            if not(i in dic_t.keys()):
                dic_t[i] = 1
            else: dic_t[i] += 1

        return dic_t == dic_s