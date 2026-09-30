class MinStack:
    def __init__(self):
        self.minstack = deque()
        self.min_val = deque()

    def push(self, val: int) -> None:
        self.minstack.append(val)
        cur = min(val, self.min_val[-1]) if self.min_val else val
        self.min_val.append(cur)
        

    def pop(self) -> None:
        self.minstack.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]

