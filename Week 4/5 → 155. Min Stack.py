class MinStack:

    def __init__(self):
        self.stk = []
        self.mnstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.mnstk:
            val = min(val, self.mnstk[-1])
        self.mnstk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.mnstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mnstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()