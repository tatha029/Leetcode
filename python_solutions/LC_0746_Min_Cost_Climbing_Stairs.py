class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f[i] = cost[i] + min(f[i+1], f[i+2])
        using, avoid = 0, 0
        for x in reversed(cost):
            using, avoid = x + min(using, avoid), using
        return min(using, avoid)
