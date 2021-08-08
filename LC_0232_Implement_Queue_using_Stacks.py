class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = 0
        self.top = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        self.size += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.top += 1
        return self.queue[self.top - 1]


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[self.top]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == self.top



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
