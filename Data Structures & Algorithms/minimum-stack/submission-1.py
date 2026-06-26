class MinStack:
    def __init__(self):
        self.minele = []
        self.l = []
 

    def push(self, val: int) -> None:
        self.l.append(val)
        if not self.minele:
            self.minele.append(val)
        else:
            self.minele.append(min(self.minele[-1],val))

    def pop(self) -> None:
        self.l.pop()
        self.minele.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.minele[-1]

