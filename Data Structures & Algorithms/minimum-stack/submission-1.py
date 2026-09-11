class MinStack:

    def __init__(self):
        self.MinStack=[]
        self.minimum=[]

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:    
            self.minimum.append(min(val,self.minimum[-1]))

    def pop(self) -> None:
        self.MinStack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]