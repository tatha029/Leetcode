class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = [2**31]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min = self.min[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min) == 1:
            return 0
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
