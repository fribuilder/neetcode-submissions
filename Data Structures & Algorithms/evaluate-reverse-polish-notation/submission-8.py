class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','*','-','/']
        stack = deque()
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == '+':
                    stack.append(a+b)
                if token == '-':
                    stack.append(b-a)
                if token == '*':
                    stack.append(b*a)
                if token == '/':
                    stack.append(b/a)

        return int(stack.pop())