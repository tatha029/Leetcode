from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # if k = 0, then return all duplicate elements
        if k == 0:
            freq = Counter(nums)
            return sum([v>1 for k, v in freq.items()])

        nums = list(set(nums))
        nums.sort()
        i, j, count = 0, 0, 0
        while j < len(nums):
            if nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else: # nums[j] - nums[i] == k
                count += 1
                j += 1
                i += 1
        return count
