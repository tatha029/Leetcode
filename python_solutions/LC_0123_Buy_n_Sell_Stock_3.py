class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = [], []
        # left pass
        min_till_now, maxProf = prices[0], 0
        for i in range(len(prices)):
            if prices[i] < min_till_now:
                min_till_now = prices[i]
            if prices[i]-min_till_now > maxProf:
                maxProf = prices[i]-min_till_now
            left.append(maxProf)
        # right pass
        max_till_now, maxProf = prices[-1], 0
        for i in reversed(range(len(prices))):
            if prices[i] > max_till_now:
                max_till_now = prices[i]
            if max_till_now - prices[i] > maxProf:
                maxProf = max_till_now - prices[i]
            right.append(maxProf)
        # sum of max_profit from left and right passes
        profit = max([x+y for x,y in zip(left, reversed(right))])
        return profit
