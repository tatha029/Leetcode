from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        queue = deque()
        res = []
        queue.append((nums[0], 0))

        for i in range(1, len(nums)):
            if queue[0][1] < i-k+1:
                queue.popleft()
            while queue and nums[i] >= queue[-1][0]:
                queue.pop()
            queue.append((nums[i], i))
            if i >= k-1:
                res.append(queue[0][0])
        return res
