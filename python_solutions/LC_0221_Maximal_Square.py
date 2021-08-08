class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # more efficient space method implies keeping only 1 row and keep track of maxSq along the way
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        maxSq = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                maxSq = max(dp[i][j], maxSq)

        return maxSq**2
