class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                newstr += s[i].lower()
        print(newstr)
        print(newstr[::-1])
        return newstr == newstr[::-1]
        