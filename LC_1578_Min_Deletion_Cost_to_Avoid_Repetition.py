class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        for i in range(len(s)-1):
            # we get identical letters
            if s[i] == s[i+1]:
                # delete the least cost
                ans += min(cost[i], cost[i+1])
                # carry forward the max cost which wasn't deleted
                cost[i+1] = max(cost[i], cost[i+1])
        return ans
