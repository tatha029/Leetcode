class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp = [[0]*n for _ in range(m)]
        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if row+1>=m and col+1>=n:
                    continue
                    # dp[row][col] = grid[row][col]
                elif row+1<m and col+1<n:
                    grid[row][col] += min(grid[row+1][col], grid[row][col+1])
                    # dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
                elif row+1<m and col+1>=n:
                    grid[row][col] += grid[row+1][col]
                    # dp[row][col] = grid[row][col] + dp[row+1][col]
                elif row+1>=m and col+1<n:
                    grid[row][col] += grid[row][col+1]
                    # dp[row][col] = grid[row][col] + dp[row][col+1]

        return grid[0][0]
        # return dp[0][0]
