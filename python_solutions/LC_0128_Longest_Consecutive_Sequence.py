class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCons = 0
        for num in numSet:
            if num-1 not in numSet:
                curNum = num
                curCons = 1
                while curNum+1 in numSet:
                    curNum += 1
                    curCons += 1
                maxCons = max(maxCons, curCons)
        return maxCons
