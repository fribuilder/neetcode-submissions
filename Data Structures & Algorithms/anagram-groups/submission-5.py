from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_count = defaultdict(list)
        res = []
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            count_tuple = tuple(count)
            dict_count[count_tuple].append(s)
        for val in dict_count.values():
            res.append(val)
        return res