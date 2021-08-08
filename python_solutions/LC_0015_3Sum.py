class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSums(nums, target):
            # we expect the nums to be sorted
            start, end = 0, len(nums)
            while start < end:
                s = nums[start] + nums[end]
                if s == target:
                    return True, start, end
                if s < target:
                    start += 1
                else:
                    end -= 1
            return False, -1, -1

        res = []
        nums.sort()
        for i in range(len(nums)-1):
            # minor improvement since nums is sorted now
            if nums[i] > 0:
                break
            found, start, end = twoSums(nums[i+1:], -nums[i])
            if found:
                res.append([i, start, end])
        return res
