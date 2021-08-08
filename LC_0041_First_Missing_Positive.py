class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        listMap = [1] + [0]*l
        for i in range(l):
            if 0 < nums[i] <= l:
                listMap[nums[i]] = 1
        for i in range(l+1):
            if listMap[i] == 0:
                return i
        return l+1
