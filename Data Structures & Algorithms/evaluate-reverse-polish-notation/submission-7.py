from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(int(ch))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if ch == '+':
                    stack.append(a + b)
                if ch == '-':
                    stack.append(a - b)
                if ch == '*':
                    stack.append(a * b)
                if ch == '/':
                    stack.append(int(a / b))
        return stack.pop()