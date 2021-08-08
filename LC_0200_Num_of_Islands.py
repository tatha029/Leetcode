class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        numIsland = 0

        def markIsland(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            markIsland(i+1, j)
            markIsland(i-1, j)
            markIsland(i, j+1)
            markIsland(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    numIsland += 1
                    markIsland(i, j)
        return numIsland
