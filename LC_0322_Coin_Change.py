class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            valid = [1+dp[i-coin] for coin in coins if i >= coin]
            if valid:
                dp[i] = min(valid)
        if dp[-1] >= amount+1:
            dp[-1] = -1
        return dp[-1]
