class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0 for _ in range(n)] for _ in range(m)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if obstacleGrid[i][j] == 1 :
                    paths[i][j] = 0
                elif i == m-1 and j == n-1 :
                    paths[i][j] = 1
                else:
                    if i == m-1:
                        pathRight = 0
                    else:
                        pathRight = paths[i+1][j]
                    if j == n-1:
                        pathDown = 0
                    else:
                        pathDown = paths[i][j+1]
                    paths[i][j] = pathRight + pathDown
        return paths[0][0]
