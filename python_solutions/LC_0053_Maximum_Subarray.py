class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_till_now, max_last = nums[0], 0
        for i in nums:
            max_last = max(i, max_last + i)
            max_till_now = max(max_till_now, max_last)
        return max_till_now
