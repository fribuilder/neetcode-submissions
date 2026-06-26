class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_words = {}
        for i, string in enumerate(strs):
            dic_string = {}
            new_string = ''.join(sorted(string))
            if new_string in dic_words:
                dic_words[new_string].append(string)
            else: dic_words[new_string] = [string]
        return list(dic_words.values())
