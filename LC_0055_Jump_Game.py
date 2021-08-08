class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, maxReached = 0, 0
        while i <= maxReached and i < len(nums):
            maxReached = max(maxReached, i + nums[i])
            if maxReached >= len(nums)-1:
                return True
            i += 1
        return False
