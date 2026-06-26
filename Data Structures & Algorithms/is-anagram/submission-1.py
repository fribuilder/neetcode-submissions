
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i],0) + 1
        for j in range(len(t)):
            dict_t[t[j]] = dict_t.get(t[j],0) + 1

        return dict_s == dict_t 

            
        