from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        cSum = 0
        hashMap[cSum] = 1
        ctr = 0
        for num in nums:
            cSum += num
            ctr += hashMap[cSum-k]
            hashMap[cSum] += 1
        return ctr
