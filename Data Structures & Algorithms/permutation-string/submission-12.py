class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count = {}
        ele = 0

        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
        
        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] = count[s2[r]] - 1
                if count[s2[r]] == 0:
                    ele += 1
            while r - l + 1 > len(s1):
                if s2[l] in count:
                    count[s2[l]] += 1
                    if count[s2[l]] == 1:
                        ele -= 1
                l += 1
                print(count, ele)
            
            if ele == len(count):
                return True
        
        return False 