class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, left, sums = 100001, 0, 0 # ans <= 10^5
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= target:
                ans = min(ans, i+1-left)
                sums -= nums[left]
                left += 1
        return ans if ans < 100001 else 0
