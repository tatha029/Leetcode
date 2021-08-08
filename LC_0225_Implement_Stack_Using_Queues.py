class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        self.loc = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.loc == self.size:
            self.stack.append(x)
            self.loc += 1
            self.size += 1
        else:
            self.stack[self.loc] = x
            self.loc += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.loc -= 1
        return self.stack[self.loc]

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[self.loc-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.loc == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
