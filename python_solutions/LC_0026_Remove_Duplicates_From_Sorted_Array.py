class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq_ptr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unq_ptr]:
                unq_ptr += 1
                nums[unq_ptr] = nums[i]
        return unq_ptr+1
