class MinStack:

    def __init__(self):
        self.stack_of_mins = []
        self.stack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_of_mins: 
            self.stack_of_mins.append(min(self.stack_of_mins[-1], val))
        else:
            self.stack_of_mins.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.stack_of_mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stack_of_mins[-1]
        
