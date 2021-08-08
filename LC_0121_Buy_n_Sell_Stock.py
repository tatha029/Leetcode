class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_till_now, max_profit = prices[0], 0
        for i in prices:
            if i-min_till_now > max_profit:
                max_profit = i-min_till_now
            if i < min_till_now:
                min_till_now = i
        return max_profit
