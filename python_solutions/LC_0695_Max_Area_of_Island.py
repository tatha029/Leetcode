class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxSize = 0

        # dfs to find island and keep track of max
        def markIsland(i, j, size):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            s1 = markIsland(i+1, j, size+1)
            s2 = markIsland(i-1, j, size+1)
            s3 = markIsland(i, j+1, size+1)
            s4 = markIsland(i, j-1, size+1)
            return 1+s1+s2+s3+s4

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = markIsland(i, j, 0)
                    maxSize = max(maxSize, size)

        return maxSize
