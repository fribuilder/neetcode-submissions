class Solution:
    def isPalindrome(self, s: str) -> bool:   
        lnum_s = ''
        for ch in s:
            if ch.isalnum():
                lnum_s += ch.lower()
        return lnum_s == lnum_s[::-1]

        