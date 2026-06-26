class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        dict2 = {}
        n = len(s1)
        for ch in s1:
            dict1[ch] = dict1.get(ch,0) + 1
        
        for ch in s2[:n]:
            dict2[ch] = dict2.get(ch,0) + 1
        
        if dict1 == dict2:
            return True
        
        for i in range(n,len(s2)):
            dict2[s2[i]] = dict2.get(s2[i],0) + 1
            dict2[s2[i-n]] = dict2.get(s2[i-n]) - 1
            if dict2[s2[i-n]] == 0:
                del dict2[s2[i-n]]
            if dict1 == dict2:
                return True

        return False
        