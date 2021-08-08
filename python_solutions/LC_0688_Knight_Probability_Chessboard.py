class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0]*N for _ in range(N)]
        dp[r][c] = 1
        nbrs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for _ in range(K):
            dp2 = [[0]*N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in nbrs:
                        if (0 <= r+dr < N) and (0 <= c+dc < N):
                            dp2[r+dr][c+dc] += val/8
            dp = dp2

        # add all elements of dp
        res = 0
        for r in range(N):
            for c in range(N):
                res += dp[r][c]
        return res
