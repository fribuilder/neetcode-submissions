class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        for ch in s: 
            if ch == '(' or ch == '{' or ch == '[':
                store.append(ch)
            elif ch == ')':
                if len(store) == 0 or store.pop(-1) != '(':
                    return False
            elif ch == ']':
                if len(store) == 0 or store.pop(-1) != '[':
                    return False
            elif ch == '}':
                if len(store) == 0 or store.pop(-1) != '{':
                    return False
        if len(store) == 0:
            return True
        else: return False
            
            

            
