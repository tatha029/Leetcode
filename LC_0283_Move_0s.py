class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_ptr] = nums[i]
                non_zero_ptr += 1
        nums[non_zero_ptr:] = [0]*(len(nums)-non_zero_ptr)
