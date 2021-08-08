class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sums = {}
        for i in range(len(nums)):
            if target-nums[i] in hash_sums:
                # given that there is always a single solution
                return [hash_sums[target-nums[i]], i]
            else:
                hash_sums[nums[i]] = i
