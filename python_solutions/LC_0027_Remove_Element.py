class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        start, end = 0, len(nums)
        while start < end:
            if nums[start] == val:
                nums[start] = nums[end-1]
                end -= 1
            else:
                start += 1
        return end
