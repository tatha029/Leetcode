class Solution:
    def rob(self, nums: List[int]) -> int:
        using, avoid = 0, 0
        for i in range(len(nums)):
            using, avoid = nums[i]+avoid, max(using, avoid)
        return max(using, avoid)
