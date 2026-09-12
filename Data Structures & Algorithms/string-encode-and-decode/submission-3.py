class Solution:
    def encode(self, strs: List[str]) -> str:
        return(''.join([f'{len(s)}#{s}' for s in strs]))

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while j < len(s):
            i = s.find('#', j)
            length = int(s[j: i])
            j = i + 1 + length
            res.append(s[i+1: j])
        return res



