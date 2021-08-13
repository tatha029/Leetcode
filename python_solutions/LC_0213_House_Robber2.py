class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # with first house
        using1, avoid1 = 0, 0
        for i in range(len(nums)-1):
            using1, avoid1 = nums[i]+avoid1, max(using1, avoid1)

        # without first house
        using2, avoid2 = 0, 0
        for i in range(1, len(nums)):
            using2, avoid2 = nums[i]+avoid2, max(using2, avoid2)

        return max(using1, avoid1, using2, avoid2)
