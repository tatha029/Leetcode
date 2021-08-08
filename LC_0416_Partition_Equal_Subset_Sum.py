class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # problem reduces to if there is a subsequence whose sum = sums(nums)/2
        if sum(nums) % 2 == 1:
            return False
        subsetSum = sum(nums)//2
        dp = [True] + [False]*subsetSum
        for num in nums:
            for target in reversed(range(num, subsetSum+1)):
                dp[target] = dp[target] or dp[target - num]
        return dp[-1]
