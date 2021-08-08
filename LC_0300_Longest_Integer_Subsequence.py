class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n**2) soln
        dp = [1]*len(nums)
        for end in range(len(nums)):
            for start in range(end):
                if nums[start] < nums[end] and dp[start] >= dp[end]:
                    dp[end] = 1 + dp[start]
        return max(dp)
