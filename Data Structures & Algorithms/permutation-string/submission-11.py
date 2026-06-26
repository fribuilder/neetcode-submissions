class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if len(s1) == 1:
            return s1 in s2

        count1 = {}
        for ch in s1: 
            count1[ch] = count1.get(ch,0) + 1

        left = 0
        right = 0
        for left in range(len(s2) - len(s1) + 1):
            print(f'left:{left}')
            while right - left < len(s1):
                print(f'right:{right}')
                if s2[right] in count1:
                    count1[s2[right]] -= 1
                if max(count1.values()) == 0 and right - left == len(s1) - 1:
                    return True
                right += 1

            if s2[left] in count1:
                count1[s2[left]] += 1
            print(count1)
            
        return False