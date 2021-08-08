class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return
        ans = []
        nums = nums + [nums[-1]]
        start, end = 0, 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                end += 1
            else:
                if start == end:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[end]))
                start, end = i, i
        return ans
