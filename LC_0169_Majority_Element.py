class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for i in nums:
            count += 1 if i == candidate else -1
            if count == 0:
                candidate, count = i, 1
        # since majority element always exists
        return candidate
