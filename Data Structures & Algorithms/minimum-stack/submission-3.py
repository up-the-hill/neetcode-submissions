class MinStack:
    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.ms:
            self.ms.append(min(val, self.ms[-1]))
        else:
            self.ms.append(val)

    def pop(self) -> None:
        self.ms.pop()
        self.s.pop()
        
    def top(self) -> int:
        return self.s[-1]
        
    def getMin(self) -> int:
        return self.ms[-1]
