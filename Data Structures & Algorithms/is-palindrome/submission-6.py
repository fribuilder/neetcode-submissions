class Solution:
    def isPalindrome(self, s: str) -> bool:   
        new = ''
        for ch in s:
            if ch.isalnum():
                new+= ch.lower()

        print(new, new[::-1])
        return new == new[::-1] 
        