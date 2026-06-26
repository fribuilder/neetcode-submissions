class Solution:
    def encode(self, strs: List[str]) -> str:
        # format each string as "<length>#<payload>"
        return ''.join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            # 1) find the next '#' which ends the length prefix
            j = s.find('#', i)
            length = int(s[i:j])
            # 2) extract exactly `length` characters after '#'
            start = j + 1
            res.append(s[start:start+length])
            # 3) advance past this chunk
            i = start + length
        return res