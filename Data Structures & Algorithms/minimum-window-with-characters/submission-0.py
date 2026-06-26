import numpy as np

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n_ch = len(set(t))
        start = 0
        contained = []
        counts_s = {}
        counts_t = {}
        min_length = np.inf
        min_str = ''
        
        for ch in t:
            counts_t[ch] = counts_t.get(ch,0) + 1

        for i, ch in enumerate(s):
            counts_s[ch] = counts_s.get(ch,0) + 1
            if (counts_t.get(ch, 0) > 0):
                if(counts_s[ch] >= counts_t[ch]) and (ch not in contained):
                    contained.append(ch)

            while len(contained) >= n_ch:
                new_length = i - start + 1
                if new_length < min_length:
                    min_length = new_length
                    min_str = s[start:i+1]
        
                counts_s[s[start]] -= 1
                
                if (counts_t.get(s[start], 0) > 0):
                    if (counts_t.get(s[start]) > counts_s[s[start]]) and (s[start] in contained):
                        contained.remove(s[start])
                        
                start += 1
        
        return min_str



        