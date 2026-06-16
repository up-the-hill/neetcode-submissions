class MinStack:

    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.history:
            self.history.append(min(self.history[-1], val))
        else:
            self.history.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.history.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.history[-1]
