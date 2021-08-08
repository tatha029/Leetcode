class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = [] # contains all elements left of median and is max heap
        self.right = [] # contains all elements right of median and is min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right, -num)
        elem = heapq.heappop(self.right)
        heapq.heappush(self.left, -elem)

        if len(self.right) < len(self.left):
            elem = heapq.heappop(self.left)
            heapq.heappush(self.right, -elem)


    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return -self.right[0]
        else:
            return (self.left[0] - self.right[0])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
